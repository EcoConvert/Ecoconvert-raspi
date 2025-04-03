from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject
from process.serial_manager import serial_manager
import time

class SerialSignal(QObject):
    """
    Signal class to handle serial data.
    """
    data_received = pyqtSignal(str)  # Signal to emit when data is received from the serial port

class SerialWorker(QRunnable):
    def __init__(self):
        super().__init__()
        # self.callback = callback  # Callback to send data to the main thread
        # self.serialManager = SerialManager()
        self.signal = SerialSignal()
        self.is_running = True

    def run(self):
        """
        Continuously read data from the serial port.
        """
        while self.is_running:
            try:
                data = serial_manager.ser.readline().decode("utf-8").strip()
                print(f'Ecobrick done?: {data}')
                if data:
                    # self.callback(data)  # Send data to the main thread
                    self.signal.data_received.emit(data)  # Emit the signal with the received data
                    # if data == '1':
                time.sleep(0.1)  # Add a small delay to avoid overloading
            except Exception as e:
                print(f"Error reading serial: {e}")
                break

    def stop(self):
        """
        Stop the worker.
        """
        self.is_running = False
        