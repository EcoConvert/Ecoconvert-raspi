# src/lcd_interface/screens/welcome_screen.py

import logging  
from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_bottle import setup_ui 
from util.state import save_state_variables
from .controller.i2_camera import CameraThread

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

class InsertScreenBottle(BaseScreen):
    """
    Welcome screen for the RVM LCD Interface.
    Displays a welcome message and initial instructions.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the welcome screen.
        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.PET_POINTS = 10.0
        self.cont = False
        logging.debug("InsertScreenBottle initialized with PET_POINTS: %.1f", self.PET_POINTS)  # Logged screen initialization
        setup_ui(self)
        self.done_clickability(False)

    def done_clickability(self, state = None):        
        if state is None:
            return
        print("Done Clickability ", state)
        logging.debug("Done button clickability set to: %s", state)  # Logged state of button enable/disable
        self.start_button.setEnabled(state)

    def _on_click(self):
        logging.debug("Start button clicked on InsertScreenBottle")  # Logged start button click
        self._capture_and_infer()

    def _capture_and_infer(self):
        logging.debug("Starting camera thread for bottle detection")  # Logged camera thread start
        pool = QThreadPool.globalInstance()
        inference = CameraThread()
        pool.start(inference)
        inference.signal.inference.connect(self.process_bottle)

    def process_bottle(self, inference = None):
        inference = False
        logging.debug("Processing bottle inference result: %s", inference)  # Logged inference result
        if inference:
            save_state_variables("bottle_exist", inference)
            logging.info("Valid bottle detected, transitioning to QR screen")  # Logged valid bottle detection
            if self.parent():
                self.parent().setCurrentIndex(4)  # go to QR Screen
                qr_screen = self.parent().widget(4)
                qr_screen.generate_qr(self.PET_POINTS)
            else:
                self.logger.warning("No parent QStackedWidget found.")  # Preserved existing warning
        else:
            logging.warning("Invalid bottle detected, transitioning to error screen")  # Logged invalid bottle event
            error_screen = self.parent().widget(7)
            error_screen.spawn_error_page(
                error_code=1,
                error_message="non 1.5 pet bottle",
                action_message="Please retrieve the non 1.5 bottle<br>then press return to standby"
            )
            self.parent().setCurrentIndex(7)
