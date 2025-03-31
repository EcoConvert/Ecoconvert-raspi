# src/lcd_interface/screens/processing_screen.py
import random
from functools import partial
import time

from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QApplication

from .base_screen import BaseScreen
from .views.processing_view import setup_ui
from util.state import save_state_variables, load_state_variables
# from serial_try import readEcoBrickWeight, ser
from process.serial_manager import readEcoBrickWeight, ser

class ProcessingScreen(BaseScreen, QObject):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        self.progress_value = 0  # Current progress value
        self.isDone = 0
        self.thread_pool = QThreadPool()
        self.worker = None
        self.timer = QTimer()
        setup_ui(self)
    
    
    # First function being called
    def wait_for_serial_done(self):
        """
        Wait for the done signal.
        """
        # self._simulate_serial_reads()
        self._serial_read()

    # def update_progress_bar(self, value):
    #     """
    #     Update the progress bar.
    #     """
    #     target_weight = 500
    #     self.progress_value = (value/target_weight * 100) - 1 # pag sinend na yung ecobrick done signal saka tayo mag +1  para maging 100 
    #     if self.progress_value >= 99:
    #         self.progress_value = 99

    #     self.progress_bar.setValue(int(self.progress_value))
    
    def _on_serial_done(self):
        self.progress_bar.setValue(100)
        # Store previous value
        bricks = load_state_variables("eco_brick_stored")
        # Increment the number of bricks
        save_state_variables("eco_brick_stored", bricks + 1)
        
        # Reset values
        self.isDone = False
        save_state_variables("weight", 0.0)
        save_state_variables("bottle_exist", False)
        standby_screen = self.parent().widget(1)
        standby_screen.pet_clickability(True)
        standby_screen.sup_clickability(True)
        self.timer.singleShot(1000, self._ready_to_go_back)

    def _ready_to_go_back(self):
        self.progress_bar.setValue(0)
        self.parent().setCurrentIndex(1)
        self.update_state(0)  


    # def _simulate_serial_reads (self):
    #     """
    #     Simulate serial reads. in the future make this a QRunabble for threading 
    #     """
    #     TimeDict = {
    #     500: 50,
    #     1000: 100,
    #     1500: 150,
    #     2000: 200,
    #     2500: 525
    #     }
    #     self.timer = QTimer()
    #     for key, val in TimeDict.items(): 
    #         self.timer.singleShot(key, partial(self.update_progress_bar, val))
    #     self.timer.singleShot(3000, self._on_serial_done) 

    def _serial_read (self):
        """
        Simulate serial reads. in the future make this a QRunabble for threading 
        """
        # self.timer = QTimer()
        # self.timer.timeout.connect(self._read_and_write())
        # self.timer.start(100)
        self.worker = SerialWorker(self._read_and_write)
        self.thread_pool.start(self.worker)
        
        
        
    def _read_and_write(self, data):
        # This is for the progress bar
        # try:
        #     weight = float(data)
        #     self.progress_value = weight / 500 * 100
        #     self.progress_bar.setValue(int(self.progress_value))
        #     if self.progress_value >= 100:
        #         self.worker.stop()
        #         self._on_serial_done()
        # except ValueError:
        #     print("Invalid data received")
        self.isDone = data
        if (self.isDone == '1'):
            self.worker.stop()
            self._on_serial_done()
        else:
            print(f"Invalid data received: {data}")
        
        
    # Always read until threshold is reached
    # while (self.progress_value < 100 and self.isDone):
    #     self.progress_value = readEcoBrickWeight() / 500 * 100 
    #     self.update_progress_bar(self.progress_value)
    #     self.timer
    #     QApplication.processEvents()
    
        # data = ser.readline().decode("utf-8").strip()
        # # If ecobrick is not yet done
        # if self.progress_value < 100:
        #     self.progress_value = data / 500 * 100
        #     self.update_progress_bar(self.progress_value)
            
        #     # Updating the GUI
        #     self.progress_bar.setValue(int(self.progress_value))
        #     print(f"Current ecobrick weight is: {self.progress_value}")
            
        # # If ecobrick weight threshold is reached
        # else:
        #     # Check for isDone flag (for storing)
        #     if not self.isDone:
        #         self.isDone = data
        #         print(f"Ecobrick storing status: {self.isDone}")
        #     else:
        #         self.timer.stop()
        #         self._on_serial_done()
                

