import os
import logging
import tensorflow as tf 
import cv2
import numpy as np
from process.modules.CameraBase import CameraBase

### DITO ILALAGAY YUNG INFERENCE IMPORTANT IMPORTANT IMPORTANT!!!
class CameraSup(CameraBase):
    def __init__(self, camera_id=0): #CHANGE THE CAM ID DEPENDS ON PORT NUMBER....
        super().__init__(camera_id)
        self.labels = {}
        self.model_path = os.getenv("MODEL_PATH")
        self.label_path = os.getenv("LABEL_PATH")
        # Load the TFLite model and allocate tensors.
        try:
            self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
            self.interpreter.allocate_tensors()
        except Exception as e:
            logging.error(f"Error loading the model: {e}")
            raise
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.camera_ready = False
        self.detection_result = []
        self.labels = {}


    def load_labels(self):
        """Load label map from a file a return a dictionary.

        Returns:
            dict: A dictionary containing the class id and class name.
        """
        try:
            with open(
                self.label_path, "r"
            ) as f:  # Changes to self.label_path, redudant to call os.getenv("LABEL_PATH") again
                for line in f:
                    if "id" in line:
                        class_id = int(line.split(":")[1].strip())
                    if "name" in line:
                        class_name = line.split("'")[1]
                        self.labels[class_id] = class_name
        except FileNotFoundError:
            logging.error(f"Error file not found: {self.label_path}")
        return self.labels
    
    def take_photo(self):
        """Take a photo using the camera"""
        if not self.camera_ready:
            logging.error("Camera is not initialized. Call init_camera() first.")
            return None, None

        ret, frame = self.camera.read()
        if not ret:
            logging.error("Error capturing frame.")
            return None, None

        input_data = self.preprocess_frame(frame)
        return frame, input_data

    def preprocess_frame(self, frame):
        """
        Preprocess the captured frame for the model.
        """
        input_shape = self.input_details[0]["shape"]
        input_tensor = cv2.resize(frame, (input_shape[1], input_shape[2]))
        input_tensor = np.expand_dims(input_tensor, axis=0)
        input_data = (np.float32(input_tensor) - 127.5) / 127.5  # Normalize to [-1, 1]
        return input_data

    def make_inference(self, input_data):
        """Make inference using the model"""
        self.interpreter.set_tensor(self.input_details[0]["index"], input_data)
        self.interpreter.invoke()

        scores = self.interpreter.get_tensor(self.output_details[0]["index"])[0]
        boxes = self.interpreter.get_tensor(self.output_details[1]["index"])[0]
        num_detections = int(
            self.interpreter.get_tensor(self.output_details[2]["index"])[0]
        )
        classes = self.interpreter.get_tensor(self.output_details[3]["index"])[0]

        self.detection_result.clear()  # Clear the previous detection results
        for i in range(num_detections):
            if scores[i] > 0.5:  # Confidence threshold
                class_id = int(classes[i]) + 1
                class_name = self.labels.get(class_id, f"Class {class_id}")
                confidence = scores[i]
                self.detection_result.append(f"{class_name}")

        if not self.detection_result:
            logging.info("No high confidence object detected.")
            return "No high confidence object detected."
        return self.detection_result[0]

    def infer(self):
        frame, input_data = self.take_photo()
        if frame is None or input_data is None:
            return "No frame captured for inference."
        return self.make_inference(input_data)

