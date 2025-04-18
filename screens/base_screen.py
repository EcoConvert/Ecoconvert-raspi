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

        # Log font loading
        self.logger.debug("Loading fonts...")

        # Poppins font
        poppins = QFontDatabase.addApplicationFont("screens/fonts/Poppins-Regular.ttf")
        self.ff_poppins = QFontDatabase.applicationFontFamilies(poppins)[0]  # use the ffs to set the font family and font size
        self.font_poppins = QFont(self.ff_poppins, 50)
        self.font_poppins.setLetterSpacing(QFont.AbsoluteSpacing, 10)

        # Log that the Poppins font is loaded
        self.logger.debug("Poppins font loaded successfully.")

        # Inter font
        inter = QFontDatabase.addApplicationFont("screens/fonts/Inter-VariableFont_opsz,wght.ttf")
        self.ff_inter = QFontDatabase.applicationFontFamilies(inter)[0]  # use the ffs to set the font family and font size
        self.font_inter = QFont(self.ff_inter, 35)
        self.font_inter.setLetterSpacing(QFont.AbsoluteSpacing, 10)

        # Log that the Inter font is loaded
        self.logger.debug("Inter font loaded successfully.")

    # Every screen has the ability to update state.
    # Not that it is needed on all screens, but it's much easier this way.
    def update_state(self, i):
        try:
            self.logger.debug(f"Attempting to update state with value: {i}")  # Log the state update attempt
            serial_manager.write(i)
            self.logger.debug("State updated successfully.")  # Log success
        except Exception as e:
            self.logger.error(f"Error updating state: {e}")  # Log error if state update fails
            print(f"Error updating state: {e}")
