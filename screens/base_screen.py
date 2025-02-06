import os
import sys
import serial


from PyQt5.QtWidgets import QWidget
from dotenv import dotenv_values, load_dotenv
from process.serial_manager import serial_manager

from util.state import * #load_state, save_state, load_state_variables, save_state_variables
from process.initialize import init_sequence 
from logging_config import lcd_logger

class BaseScreen(QWidget):
    """
    Base Class for all screens in the RVM LCD Interface.

    Handles common functionality such as configuration, camera access, and logging.
    """

    # What is parent?
    def __init__(self, config, parent=None, camera=None):
        """
        Initialize the base screen.

        Args:
            config (dict): Application Configuration.
            parent (QWidget, optional): Parent Widget (example QStackedWidget).
            camera (Camera, optional): Camera instance for specific screen
        """
        super().__init__(parent)
        self.state = None
        self.config = config
        self.camera = camera
        self.logger = lcd_logger(self.__class__.__name__)

        # Common debug log
        self.logger.debug(f"Initialized {self.__class__.__name__}")

    # every screen has the ability to update state. 
    # not that it is needed on all screen, but its much easier this way. 
    def update_state(self, i): 
        try:
            serial_manager.write(i) 
        except Exception as e:
            print(f"Error updating state: {e}")
    