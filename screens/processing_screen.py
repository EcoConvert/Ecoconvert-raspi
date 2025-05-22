import random
from functools import partial
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication
from .base_screen import BaseScreen
from .views.processing_view import setup_ui
from util.state import save_state_variables, load_state_variables
from logging_config import lcd_logger 

class ProcessingScreen(BaseScreen):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this screen
        self.progress_value = 0  # Current progress value
        self.logger.debug("Initializing Processing Screen")  # Log screen initialization
        setup_ui(self)
    
    def wait_for_serial_done(self):
        """
        Wait for the done signal.
        """
        self.logger.info("Waiting for serial done signal")  # Log when waiting for serial done signal
        self._simulate_serial_reads()

    def update_progress_bar(self, value):
        """
        Update the progress bar.
        """
        target_weight = 500
        self.progress_value = (value / target_weight * 100) - 1  # pag sinend na yung ecobrick done signal saka tayo mag +1  para maging 100 
        if self.progress_value >= 99:
            self.progress_value = 99
        
        self.progress_bar.setValue(int(self.progress_value))
        self.logger.debug(f"Updated progress bar value to {self.progress_value}%")  # Log progress bar update
    
    def _on_serial_done(self):
        self.progress_bar.setValue(100)
        bricks = load_state_variables("eco_brick_stored")  
        save_state_variables("eco_brick_stored", bricks + 1)
        save_state_variables("weight", 0.0)
        save_state_variables("bottle_exist", False)
        self.logger.info("Serial done")  # Log serial done event
        
        standby_screen = self.parent().widget(1)
        standby_screen.pet_clickability(True)
        standby_screen.sup_clickability(True)
        self.timer.singleShot(1000, self._ready_to_go_back)

    def _ready_to_go_back(self):
        self.progress_bar.setValue(0)
        self.parent().setCurrentIndex(1) # Standby Screen
        self.update_state(0)
        self.logger.info("Ready to go back to standby screen: Progress bar reset")  # Log ready to standby screen :* mwah

    def _simulate_serial_reads(self):
        """
        Simulate serial reads. in the future make this a QRunnable for threading 
        """
        self.logger.debug("Simulating serial reads")  # Log when serial reads are being simulated
        TimeDict = {
            2000: 50,
            4000: 100,
            6000: 150,
            8000: 200,
            10000: 525
        }
        self.timer = QTimer()
        for key, val in TimeDict.items(): 
            self.timer.singleShot(key, partial(self.update_progress_bar, val))
        self.timer.singleShot(15000, self._on_serial_done)
        self.logger.debug("Scheduled simulated serial reads and progress updates")  # Log scheduling of serial reads and ung progress bar