import logging
import os

import cv2
import numpy as np
import tensorflow as tf

from process.modules.CameraBase import CameraBase

# Define log directory path -> Mababago pa
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../logs"))

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=os.path.join(log_dir, "camera_sup.log"),
)

### DITO ILALAGAY YUNG INFERENCE IMPORTANT IMPORTANT IMPORTANT!!!
class CameraSup(CameraBase):
    def __init__(self, camera_id=0): #CHANGE THE CAM ID DEPENDS ON PORT NUMBER....
        super().__init__(camera_id)
        self.model_path = os.getenv("MODEL_PATH_DETECTION")
        self.label_path = os.getenv("LABEL_PATH")

        self.labels = {}
        self.camera_ready = False
        self.detection_result = [] 
        self.labels = {}
        self._setup_model()
        self._load_labels() 

    def _setup_model(self):
        """
        Initialize TF
        """

        try:
            self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
            self.interpreter.allocate_tensors()

            # Get input output details
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()

            input_info = self.input_details[0]
            logging.info(f"Model Loaded: {input_info['name']}")
            logging.info(f"INPUT DETAILS: Shape - {input_info['shape']} | dtype - {input_info['dtype']}")
            logging.info(f"OUTPUT DETAILS: {self.output_details}")
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise
        
    def _load_labels(self):
        """Load label map from a file and return a dictionary."""
        self.labels = {}
        try:
            logging.info(f"Attempting to load labels from {self.label_path}")
            with open(self.label_path, "r") as f:
                class_id = None
                for line in f:
                    line = line.strip()
                    if line.startswith("id:"):
                        class_id = int(line.split(":")[1].strip())
                    elif line.startswith("name:") and class_id is not None:
                        # Handles 'name: "plastic"' or 'name: 'plastic''
                        class_name = line.split(":")[1].strip().strip('"').strip("'")
                        self.labels[class_id] = class_name
                        class_id = None
        except FileNotFoundError:
            logging.error(f"Label file not found: {self.label_path}")
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
        resized = cv2.resize(frame, (input_shape[2], input_shape[1]))
        input_tensor = np.expand_dims(resized.astype(np.float32), axis=0)
        normalized = (input_tensor / 127.5) - 1.0
        return normalized

    def make_inference(self, input_data, frame):
        """Make inference using the model"""
        self.interpreter.set_tensor(self.input_details[0]["index"], input_data)
        self.interpreter.invoke()

        scores = self.interpreter.get_tensor(self.output_details[0]["index"])[0]
        boxes = self.interpreter.get_tensor(self.output_details[1]["index"])[0]
        num_detections = int(
            self.interpreter.get_tensor(self.output_details[2]["index"])[0]
        )
        classes = self.interpreter.get_tensor(self.output_details[3]["index"])[0]
        logging.info(f"Classes: {classes[:num_detections]}")
        logging.info(f"Scores: {scores[:num_detections]}")
        logging.info(f"Boxes: {boxes[:num_detections]}")

        self.detection_result.clear()  # Clear the previous detection results
        for i in range(num_detections):
            if scores[i] > 0.2:  # Confidence threshold
                class_id = int(classes[i]) # + 1 -> adjusted label map for 0: metal, 1: plastic
                class_name = self.labels.get(class_id, f"Class {class_id}")
                confidence = scores[i]
                logging.info("[Camera_Sup.py] self.labels: ", self.labels)
               
                # # class_name = self.labels.get(class_id)
                # confidence = scores[i]

                # For drawing box
                y_min, x_min, y_max, x_max = boxes[i]
                h, w, _ = frame.shape
                x_min = int(x_min * w)
                x_max = int(x_max * w)
                y_min = int(y_min * h)
                y_max = int(y_max * h)

                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                # Can be use padin if result lang kukunin
                #self.detection_result.append(f"{class_name}")

        if not self.detection_result:
            logging.info("No high confidence object detected.")
            return "No high confidence object detected.", frame
        return self.detection_result[0], frame

    def infer(self, display=False):
        frame, input_data = self.take_photo()
        if frame is None or input_data is None:
            return "No frame captured for inference."

        result, output_frame = self.make_inference(input_data, frame)

        if display:
            cv2.imshow("Detection", output_frame)
            cv2.waitKey(1)

            
        # return self.make_inference(input_data)
        return result



