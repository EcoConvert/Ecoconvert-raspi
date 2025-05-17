from PyQt5.QtCore import QRunnable, pyqtSignal, QObject
from process.modules.Camera_YSup import CameraSup

class s_inference_signal(QObject):
    inference = pyqtSignal(bool)

class i_signal(QObject):
    initDone= pyqtSignal(bool)

class SharedCamera:
    """Singleton-like object to store a shared camera instance"""
    camera = None

class CamInitThread2(QRunnable):
    """Thread to initialize and open the camera"""
    def __init__(self):
        super().__init__()
        self.signal = s_inference_signal()
        self.signal = i_signal()
    def run(self):
        print("Camera init")
        if SharedCamera.camera is None:  # Ensure the camera is only initialized once
            SharedCamera.camera = CameraSup()
        SharedCamera.camera.init_camera()
        self.signal.initDone.emit(True)

class CameraThread2(QRunnable): 
    """Thread to take a photo and perform inference"""
    def __init__(self):
        super().__init__()
        self.signal = s_inference_signal()

    def run(self):
        if SharedCamera.camera is None:
            print("Camera not initialized")
            return
        obj_det_result = SharedCamera.camera.infer()  # Capture and process
        
        if "metal" in obj_det_result or "rock" in obj_det_result or "trash" in obj_det_result:
            # print("Metal, rock, or trash detected")
            self.signal.inference.emit(False)
        else:
            # print(f"Object detected: {obj_det_result}")
            self.signal.inference.emit(True)
        SharedCamera.camera.release_camera()