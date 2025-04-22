
import cv2

from process.modules.Camera_Sup import CameraSup

cam = CameraSup(camera_id=0)
cam.init_camera()  # Make sure CameraBase defines this method

try:
    while True:
        result = cam.infer()
        print("Detected:", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cam.release_camera()
    cv2.destroyAllWindows()
