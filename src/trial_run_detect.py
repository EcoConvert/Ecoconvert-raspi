
import cv2

from src.module.cameraSUP1 import CameraSup

cam = CameraSup(camera_id=2)
cam.init_camera()

# Capture a frame
cam.take_photo()

# Process the same frame multiple times
result1 = cam.infer()  # Uses stored frame
result2 = cam.infer(conf_threshold=0.5)  # Different threshold, same frame
result3 = cam.infer(conf_threshold=0.7)  # Different threshold, same frame

# Display with bounding boxes but don't get results
cam.process_current_frame(display=True)

# When ready for a new frame
result4 = cam.infer(new_capture=True)  # Captures a new frame

if "metal" in result1:
    print("METAL")