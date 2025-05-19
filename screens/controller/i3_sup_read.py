from PyQt5.QtCore import QRunnable, pyqtSignal, QObject
from process.serial_manager import serial_manager

class weight_reading(QObject):
    weight = pyqtSignal(float)


class SupSerialReadThread(QRunnable):
    """Thread to Read serial until 8 byte char is filled"""
    def __init__(self):
        super().__init__()
        self.signal = weight_reading()
        self.done = False
    def run(self):
        print("Camera init")
        while not self.done:
            weight =  serial_manager.readSUPWeight()
            self.signal.weight.emit(weight)
            print("weight to: ",weight)
            self.done = True; 

