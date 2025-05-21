# admin_password_screen.py

import os
import dotenv
from PyQt5.QtCore import QTimer

from logging_config import lcd_logger

from .base_screen import BaseScreen
from .views.admin_password_view import setup_ui



class AdminPasswordScreen(BaseScreen):
    """
    Admin Password Screen for the RVM LCD Interface
    Prompt the user for 
    """
    def __init__(self, config, parent=None):
        super().__init__(config, parent)

        setup_ui(self)

        self.correct_password = os.getenv("PASSWORD")  # Temp -> Transfer to .env
        self.tries = 0
        self.logger = lcd_logger(__name__)
        self.logger.debug("Admin Password Screen initialized.")
        self.submit_btn.clicked.connect(self.verify_password)

    def reset_and_return(self):
        self.tries = 0
        self.password_input.clear()
        self.password_label.setText("Enter Admin Password")

        if self.parent():
            self.parent().setCurrentIndex(0)

    def verify_password(self):
        input_password = self.password_input.text()
        if input_password == self.correct_password :
            self.logger.info("Access Granted")
            parent = self.parent()
            if parent:
                parent.setCurrentIndex(8)  # For example, admin dashboard
        else:
            self.tries += 1
            self.logger.warning(f"Incorrect admin password attempt {self.tries}/3")

            if self.tries >= 3:
                self.password_label.setText("Not an admin. Returning in 5 seconds")

                QTimer.singleShot(5000, self.reset_and_return)
            else:
                self.password_label.setText("Incorrect password. Try again")
                self.password_input.clear()
                

    
