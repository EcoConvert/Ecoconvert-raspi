import logging 
import os
import cv2
import numpy as np
import tensorflow as tf
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class Camera:   
    # I want to use type annotations, but the required version of python that the  tensorflow for needs is 3.9. WE NEED 3.10 for type annotations 
    def __init__(self, camera_id = 0 ):
        """ Load the model"""
        self.camera_ready = False
        self.camera_id = camera_id
        # error handles it it does not open
        self.model_path = os.getenv("MODEL_PATH")
        self.label_path = os.getenv("LABEL_PATH")

        # Load the TFLite model
        self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()
        
        # Get input and output tensors
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.labels = {}
        self.detection_result = []
        
    def load_labels(self):
        """
        Load label map from a file.
        """
        with open(os.getenv("LABEL_PATH"), 'r') as f:
            for line in f:
                if "id" in line:
                    class_id = int(line.split(":")[1].strip())
                if "name" in line:
                    class_name = line.split("'")[1]
                    self.labels[class_id] = class_name
            return self.labels

    def init_camera(self):
        """Initialize the camera this needs to happen at the very beginning of the program"""
        self.camera = cv2.VideoCapture(self.camera_id)
        # handle error if the camera does not open    
        self.camera_ready = True
        

    def take_photo(self):
        """Take a photo using the camera"""
        ret, frame = self.camera.read()
        if not ret:
            # handle error if the camera does not take a photo
            return None
        input_data = self.preprocess_frame(frame)
        return frame, input_data

    def preprocess_frame(self, frame):
        """
        Preprocess the captured frame for the model.
        """

        input_shape = self.input_details[0]['shape']
        input_tensor = cv2.resize(frame, (input_shape[1], input_shape[2]))
        input_tensor = np.expand_dims(input_tensor, axis=0)
        input_data = (np.float32(input_tensor) - 127.5) / 127.5  # Normalize to [-1, 1]
        return input_data

    def make_inference(self, input_data):
        """Make inference using the model"""
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        
        scores = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        boxes = self.interpreter.get_tensor(self.output_details[1]['index'])[0]
        num_detections = int(self.interpreter.get_tensor(self.output_details[2]['index'])[0])
        classes = self.interpreter.get_tensor(self.output_details[3]['index'])[0]

        for i in range(num_detections):
            if scores[i] > 0.5:  # Confidence threshold
                class_id = int(classes[i])
                class_name = self.labels.get(class_id, f"Class {class_id}")
                confidence = scores[i]
                self.detection_result.append(f"Object: {class_name}, Confidence: {confidence:.2f}")
        
        return '\n'.join(self.detection_result) if self.detection_result else "No high confidence objects detected."

    def capture_and_infer(self):
        """This is the only method that should be called. Capture a photo and make inference."""
        frame, input_data = self.take_photo()
        result = self.make_inference(input_data)
        return result

    def release_camera(self):
        """Release the camera"""
        if self.camera_ready:
            self.camera.release()
            self.camera_ready = False
            print("Camera released.")
