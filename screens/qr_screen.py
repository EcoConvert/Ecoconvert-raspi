# src/lcd_interface/screens/welcome_screen.py
import datetime
import os

import jwt
import qrcode
from dotenv import load_dotenv
from PIL import Image

from .base_screen import BaseScreen
from .views.qr__view import setup_ui 


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
        self.generate_qr(15)
    
    def _on_click(self):
        if self.parent():
            self.update_state(0) # update to standby
            standby_screen = self.parent().widget(1)
            # implement conditional showing of button
            standby_screen.global_state_checker() # <-screen changer  is on this one 
        else:
            self.logger.warning("No parent QStackedWidget found.")

    def generate_qr(self, point):
        print("generating qr")  
        self.pointsLabel.setText(f"Points: {point}")
        payload = {
            "points": point,
            "iat": int(datetime.datetime.now().timestamp()),
        }
        valid_token = jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")
        print(valid_token)

        # Generate QR Code
        qr = qrcode.make(valid_token)
        qr_path = "token.png"
        qr.save(qr_path)
        print("QR Code saved as 'toksen.png'")

        return qr_path
