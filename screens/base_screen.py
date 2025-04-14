import os
import sys
import serial

from PyQt5.QtWidgets import QWidget
from dotenv import dotenv_values, load_dotenv
from process.serial_manager import serial_manager

from util.state import * #load_state, save_state, load_state_variables, save_state_variables
from logging_config import lcd_logger
from PyQt5.QtGui import QFontDatabase, QFont


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

        # create fonts here
        try:
            # Poppins
            self.logger.debug("Loading Poppins font...")
            poppins = QFontDatabase.addApplicationFont("screens/fonts/Poppins-Regular.ttf")
            self.ff_poppins = QFontDatabase.applicationFontFamilies(poppins)[0]
            self.font_poppins = QFont(self.ff_poppins, 50)
            self.font_poppins.setLetterSpacing(QFont.AbsoluteSpacing, 10)
            self.logger.debug("Poppins font loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load Poppins font: {e}")

        try:
            # Inter
            self.logger.debug("Loading Inter font...")
            inter = QFontDatabase.addApplicationFont("screens/fonts/Inter-VariableFont_opsz,wght.ttf")
            self.ff_inter = QFontDatabase.applicationFontFamilies(inter)[0]
            self.font_inter = QFont(self.ff_inter, 35)
            self.font_inter.setLetterSpacing(QFont.AbsoluteSpacing, 10)
            self.logger.debug("Inter font loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load Inter font: {e}")

    # every screen has the ability to update state. 
    # not that it is needed on all screen, but its much easier this way. 
    def update_state(self, i): 
        self.logger.debug(f"Attempting to update state with value: {i}")
        try:
            serial_manager.write(i) 
            self.logger.debug(f"State updated with value: {i}")
        except Exception as e:
            self.logger.error(f"Error updating state: {e}")
            print(f"Error updating state: {e}")
