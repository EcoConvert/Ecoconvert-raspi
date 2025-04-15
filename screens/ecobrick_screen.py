# src/lcd_interface/screens/welcome_screen.py

import logging  
from .base_screen import BaseScreen
from .views.ecobrick_view import setup_ui

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG)

class EcoScreen(BaseScreen):
    """
    Ecobrick Retrieve screen
    """
    
    def __init__(self, config, parent=None):
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.ecobrick = 0
        logging.debug("EcoScreen initialized")  # Logging
        setup_ui(self)
    
    def _on_click(self):
        logging.debug("Button clicked in EcoScreen")  # Logging
        if self.parent():
            self.parent().setCurrentIndex(1)
