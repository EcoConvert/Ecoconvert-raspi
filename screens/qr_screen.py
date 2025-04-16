# src/lcd_interface/screens/qr_screen.py
import datetime
import os
import logging  

import jwt
import qrcode
from dotenv import load_dotenv
# from PIL import Image

from .base_screen import BaseScreen
from .views.qr__view import setup_ui 
from PyQt5.QtGui import QPixmap


class QrScreen(BaseScreen):
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
        self.points = 0
        setup_ui(self)
        load_dotenv(override=True)

        # Load secret key
        self.SECRET_KEY = os.getenv("SECRET_KEY")

        # <-- Logging: Logger setup added here
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        self.logger.info("QrScreen initialized.")

    
    def _on_click(self):
        if self.parent():
            self.update_state(0) # update to standby
            standby_screen = self.parent().widget(1)
            # implement conditional showing of button
            standby_screen.global_state_checker() # <-screen changer  is on this one 
            self.logger.info("Navigated to standby screen.")  # Logging
        else:
            self.logger.warning("No parent QStackedWidget found.")  # Logging

    def generate_qr(self, point):
        # print("generating qr")  
        self.pointsLabel.setText(f"Points: {point}")
        payload = {
            "points": point,
            "iat": int(datetime.datetime.now().timestamp()),
        }
        valid_token = jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")
        # print(valid_token)
        self.logger.info("JWT generated for points: %s", point)  # Logging

        # Generate QR Code
        qr = qrcode.make(valid_token)
        qr_path = "screens/qr_img/token.png"
        qr.save(qr_path)
        # print("QR Code saved as 'token.png'")
        self.logger.info("QR code saved at %s", qr_path)  # Logging
        self._change_token_image(qr_path)

    def _change_token_image(self, filepath):  
        self.qr.setPixmap(QPixmap(filepath))   #mot was here
        self.logger.info("QR image updated on screen from %s", filepath)  # Logging
