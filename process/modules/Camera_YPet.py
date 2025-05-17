"""
CameraPet module for PET bottle detection and classification.
"""

import logging
import os
import time

import cv2
import numpy as np
# import tensorflow as tf
from dotenv import load_dotenv
from ultralytics import YOLO

from process.modules.CameraBase import CameraBase

# Define log directory path
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../logs"))

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=os.path.join(log_dir, "camera_pet.log"),
)

class CameraPet(CameraBase):
    """
    A class for detecting and classifying PET bottles.
    """
    
    def __init__(self, camera_id=0, model_path=None):
        """
        Initialize the CameraPet detector.
        
        Args:
            camera_id: Camera device index
            model_path: Path to the YOLO model file
        """
        super().__init__(camera_id)
        # Set model path from ENV
        self.model_path = model_path or os.getenv("MODEL_PATH_CLASSIFICATION")
        if not self.model_path:
            logging.error("Model path not provided")
            raise ValueError(("Model path not provided"))

            
        # Initialize parameters for PET bottle
        self.fgbg = None
        self.detection_triggered = None
        self.frame_counter = 0
        self.prediction_result = None
        
        # Configure ROI and thresholds
        self.roi_config = {
            "x1": 230, "y1": 40,
            "x2": 370, "y2": 100,
            "area_threshold": 500,
            "time_threshold": 1.0
        }

        # Setup Morphological kernel
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

        
        self._setup_model()

    def _setup_model(self):
        """Initialize the YOLO model for classification."""
        
        try:
            self.model = YOLO(self.model_path)
            logging.info(f"YOLO model loaded from: {self.model_path}")
        except Exception as e:
            logging.error(f"Error loading YOLO model: {e}")
            raise

    def _run_inference(self, frame):
        """
        Run inference on the frame using YOLO model.
        
        Args:
            frame: Image frame to analyze
            
        Returns:
            class_label, confidence, inference_time
        """
        try:
            # Get the start time
            start_time = time.perf_counter()

            # Get the results
            # Basically ganyan lang siya mag predict
            results = self.model(frame)

            # Get the best prediction
            probs = results[0].probs.data.tolist()

            # Get the class name
            class_names = results[0].names
            
            # Get predicted class index
            pred_class = int(np.argmax(probs))
            confidence = float(probs[pred_class])

            # Get class name from index
            class_label = class_names[pred_class]

            # Calculate total inference time
            end_time = time.perf_counter()
            inference_time = (end_time - start_time) * 1000 # Convert to MS

            logging.info(f"Inference time: {inference_time:.3f} ms")
            logging.info(f"Prediction: {class_label} -> ({confidence:.4f})")

            return class_label, confidence, inference_time
            
        except Exception as e:
            logging.error(f"Error during inference: {e}")
            return None, None, None

    def _setup_detection(self):
        """Initialize background subtractor and frame threshold."""
        # Create background subtractor
        self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

        # calculate frame threshold based on camera fps
        if self.camera_ready:
            fps = self.camera.get(cv2.CAP_PROP_FPS)
            self.frame_threshold = int(self.roi_config["time_threshold"] * fps)
        else:
            # Default to 30 fps
            self.frame_threshold = int(self.roi_config["time_threshold"] * 30)
            
    def _process_roi(self, frame):
        """
        Process the region of interest to detect objects.
        
        Args:
            frame: Image frame to analyze
            
        Returns:
            roi_mask, total_area
        """
        fgmask = self.fgbg.apply(frame)
        # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
        # fgmask = cv.morphologyEx(fgmask, cv.MORPH_CLOSE, kernel)
        fgmask = cv2.dilate(fgmask, self.kernel, iterations=1)

        # Extrract the ROI from the mask
        x1, y1 = self.roi_config["x1"], self.roi_config["y1"]
        x2, y2 = self.roi_config["x2"], self.roi_config["y2"]
        roi_mask = fgmask[y1:y2, x1:x2]

        # Find contours in the ROI
        contours, _ = cv2.findContours(roi_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Calculate total area of significant contours
        total_area = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300:  # Filter small noise
                total_area += area
                
        return roi_mask, total_area 

    def infer(self, timeout=10.0, display=True):
        """
        Detect and classify PET bottles.
        
        Args:
            timeout: Maximum wait time in seconds
            display: Whether to show visual output
            
        Returns:
            Dictionary with classification results
        """
        logging.info("Starting PET bottle detection and classification")
         
        # Initialize camera
        if not self.camera_ready:
            self.init_camera()

        # Setup detection paramters
        self._setup_detection()
        
        # Reset detection state
        self.detection_triggered = False
        self.frame_counter = 0
        # For timeout
        start_time = time.time()

        try:
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    logging.error("Failed to capture frame")
                    break

                # Check for timeout
                current_time = time.time()
                if not self.detection_triggered and (current_time - start_time > timeout):
                    self.prediction_result = {
                        "class": 'unacceptable',
                        "score": 0.0,
                        "inference_time": 0.0,
                        "reason": "no object",
                    }
                    self.detection_triggered = True
                    logging.info("Detection timeout reached or bottle")
                    break
            
                # Create a copy for visualziation
                frame_with_roi = frame.copy()

                # PRocess the region of intereset
                roi_mask, total_area = self._process_roi(frame)
                # Display frame with ROI
                if display:
                    x1, y1 = self.roi_config['x1'], self.roi_config['y1']
                    x2, y2 = self.roi_config['x2'], self.roi_config['y2']
                    cv2.rectangle(frame_with_roi, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                # Object persistence check
                if total_area > self.roi_config['area_threshold']:
                    self.frame_counter += 1
                    
                    # Show detection progress
                    if display:
                        cv2.putText(frame_with_roi, f"Detecting: {self.frame_counter}/{self.frame_threshold}", 
                                   (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    
                    # Check if detection threshold reached
                    if self.frame_counter >= self.frame_threshold and not self.detection_triggered:
                        # Run inference
                        class_label, score, inference_time = self._run_inference(frame)
                        
                        if class_label is not None:
                            self.prediction_result = {
                                "class": class_label,
                                "score": float(score),
                                "inference_time": float(inference_time),
                                "reason": "detected"
                            }
                            self.detection_triggered = True
                            
                            # Display prediction
                            if display:
                                cv2.putText(frame_with_roi, f"Prediction: {class_label} ({score:.2f})", 
                                           (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
                            
                            break
                else:
                    # Reset counter if object disappears
                    self.frame_counter = 0
                    if display:
                        cv2.putText(frame_with_roi, "Waiting for object...", (30, 30), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
                
                # Display frames if requested
                if display:
                    cv2.imshow("ROI Mask", roi_mask)
                    cv2.imshow("Frame", frame_with_roi)
                
                # Check for keyboard input
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                elif key == ord("c"):
                    # Force manual classification
                    class_label, score, inference_time = self._run_inference(frame)
                    
                    if class_label is not None:
                        self.prediction_result = {
                            "class": class_label,
                            "score": float(score),
                            "inference_time": float(inference_time),
                            "reason": "manual"
                        }
                        
                        if display:
                            result_frame = frame.copy()
                            cv2.putText(result_frame, f"Manual: {class_label} ({score:.2f})", 
                                       (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            cv2.imshow("Manual Result", result_frame)
                        
                        break
            
            return self.prediction_result
            
        except Exception as e:
            logging.error(f"Error during operation: {e}")
            return {"class": "error", "reason": str(e)}
        finally:
            # Clean up windows but don't release camera
            if display:
                cv2.destroyAllWindows()
    
    def get_last_prediction(self):
        """
        Get the last prediction result.
        
        Returns:
            Last prediction result or None
        """
        return self.prediction_result