# src/lcd_interface/screens/processing_screen.py
import random
import logging 
from functools import partial

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication

from .base_screen import BaseScreen
from .views.processing_view import setup_ui
from util.state import save_state_variables, load_state_variables

# Basic logger setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ProcessingScreen(BaseScreen):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        self.progress_value = 0  # Current progress value
        setup_ui(self)
        logger.info("ProcessingScreen initialized.")  # Logging

    def wait_for_serial_done(self):
        """
        Wait for the done signal.
        """
        logger.info("Waiting for serial done signal...")  # Logging
        self._simulate_serial_reads()

    def update_progress_bar(self, value):
        """
        Update the progress bar.
        """
        target_weight = 500
        self.progress_value = (value / target_weight * 100) - 1
        if self.progress_value >= 99:
            self.progress_value = 99

        self.progress_bar.setValue(int(self.progress_value))
        logger.info(f"Progress bar updated: {self.progress_value:.2f}%")  # Logging

    def _on_serial_done(self):
        self.progress_bar.setValue(100)
        logger.info("Serial done. Progress bar set to 100%.")  # Logging

        bricks = load_state_variables("eco_brick_stored")
        save_state_variables("eco_brick_stored", bricks + 1)
        save_state_variables("weight", 0.0)
        save_state_variables("bottle_exist", False)

        logger.info("State variables updated after completion.")  # Logging

        standby_screen = self.parent().widget(1)
        standby_screen.pet_clickability(True)
        standby_screen.sup_clickability(True)

        self.timer.singleShot(1000, self._ready_to_go_back)

    def _ready_to_go_back(self):
        self.progress_bar.setValue(0)
        logger.info("Returning to standby screen.")  # Logging
        self.parent().setCurrentIndex(1)
        self.update_state(0)

    def _simulate_serial_reads(self):
        """
        Simulate serial reads. In the future, make this a QRunnable for threading.
        """
        logger.info("Simulating serial reads...")  # Logging

        TimeDict = {
            500: 50,
            1000: 100,
            1500: 150,
            2000: 200,
            2500: 525
        }

        self.timer = QTimer()
        for key, val in TimeDict.items():
            self.timer.singleShot(key, partial(self.update_progress_bar, val))
            logger.debug(f"Scheduled update: time={key}ms, value={val}")  # Logging

        self.timer.singleShot(3000, self._on_serial_done)
