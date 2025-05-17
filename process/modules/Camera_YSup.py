
import logging
import os

import cv2
import numpy as np
from ultralytics import YOLO

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

class CameraSup(CameraBase):
    def __init__(self, camera_id=0, conf_threshold=0.2):
        super().__init__(camera_id)
        self.model_path = os.getenv("MODEL_PATH_DETECTION")  # Path to YOLO model
        self.camera_ready = False
        self.detection_result = []
        self.conf_threshold = conf_threshold
        self.current_frame = None  # Store the current frame
        self._setup_model()
        
    def _setup_model(self):
        try:
            self.model = YOLO(self.model_path)
            logging.info(f"YOLO Model Loaded: {self.model_path}")
            logging.info(f"Model classes: {self.model.names}")
        except Exception as e:
            logging.error(f"Error loading YOLO model: {e}")
            raise

    def take_photo(self):
        if not self.camera_ready:
            logging.error("Camera is not initialized. Call init_camera() first")
            return None
        
        ret, frame = self.camera.read()
        if not ret:
            logging.error("Failed to capture frame")
            return None
        
        # Store the captured frame for reuse
        self.current_frame = frame.copy()
        return frame
    
    def make_inference(self, frame=None, conf_threshold=None):
        """
        Process the current frame with object detection
        
        Args:
            frame: Optional frame to use instead of stored frame
            conf_threshold: Optional confidence threshold override
        """
        # Use provided frame or the stored one
        if frame is None:
            frame = self.current_frame
            
        if frame is None:
            logging.error("No frame available for inference")
            return None
            
        threshold = conf_threshold if conf_threshold is not None else self.conf_threshold
        results = self.model(frame)
        
        # Create a copy for drawing if we need to display
        display_frame = frame.copy()
        
        self.detection_result.clear()
        result = results[0]
        boxes = result.boxes
        
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy() 
            
            # Confidence score
            conf = float(box.conf[0])
            if conf > threshold:
                cls = int(box.cls[0])
                class_name = self.model.names[cls]
                
                # Draw box on the display frame
                x_min, y_min, x_max, y_max = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(display_frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                label = f"{class_name}: {conf:.2f}"
                cv2.putText(display_frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
                # Just add the class name to detection results
                self.detection_result.append(class_name)
        
        return self.detection_result, display_frame
        
    def capture_and_infer(self, display=True, conf_threshold=None):
        """
        Capture a new frame and perform inference
        
        Args:
            display: Whether to display the output frame
            conf_threshold: Optional confidence threshold override
        """
        frame = self.take_photo()
        if frame is None:
            return []
            
        return self.process_current_frame(display, conf_threshold)
    
    def process_current_frame(self, display=True, conf_threshold=None):
        """
        Process the currently stored frame
        
        Args:
            display: Whether to display the output frame
            conf_threshold: Optional confidence threshold override
        """
        if self.current_frame is None:
            return []
            
        detections, output_frame = self.make_inference(conf_threshold=conf_threshold)
        try:    
            if display and output_frame is not None:
                cv2.imshow("Detection", output_frame)
                cv2.waitKey(1)
                
            return detections
        except Exception as e:
            logging.error(f"Error displaying frame: {e}")
            return []
        finally:
            if display:
                cv2.destroyAllWindows()

    def infer(self, display=False, conf_threshold=None, new_capture=False):
        """
        Perform inference on current or new frame
        
        Args:
            display: Whether to display the output frame
            conf_threshold: Optional confidence threshold override
            new_capture: Whether to capture a new frame or use the stored one
        
        Returns:
            A list of detected class names
        """
        if new_capture or self.current_frame is None:
            return self.capture_and_infer(display, conf_threshold)
        else:
            return self.process_current_frame(display, conf_threshold)