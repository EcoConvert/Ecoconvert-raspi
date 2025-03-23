from PyQt5.QtCore import QRunnable, pyqtSignal, QObject
from process.modules.Camera_Pet import CameraPet

class p_inference_signal(QObject):
    inference = pyqtSignal(bool)

class i_signal(QObject):
    initDone= pyqtSignal(bool)

class SharedCamera:
    """Singleton-like object to store a shared camera instance"""
    camera = None

class CamInitThread(QRunnable):
    """Thread to initialize and open the camera"""
    def __init__(self):
        super().__init__()
        self.signal = p_inference_signal()
        self.signal = i_signal()
    def run(self):
        print("Camera init")
        if SharedCamera.camera is None:  # Ensure the camera is only initialized once
            SharedCamera.camera = CameraPet()
        SharedCamera.camera.init_camera()
        self.signal.initDone.emit(True)

class CameraThread(QRunnable): 
    """Thread to take a photo and perform inference"""
    def __init__(self):
        super().__init__()
        self.signal = p_inference_signal()

    def run(self):
        if SharedCamera.camera is None:
            print("Camera not initialized")
            return
        valid = SharedCamera.camera.infer()  # Capture and process
        self.signal.inference.emit(valid)
        SharedCamera.camera.release_camera()