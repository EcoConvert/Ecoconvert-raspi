# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.ecobrick_view import setup_ui
from logging_config import lcd_logger  

class EcoScreen(BaseScreen):
    """
    Ecobrick Retrieve screen
    """
    
    def __init__(self, config, parent=None):
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.ecobrick = 0
        self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this screen
        self.logger.debug("Initializing EcoScreen")  # Log when EcoScreen is initialized
        setup_ui(self)
    
    def _on_click(self):
        """
        Handle the click event to navigate to the next screen.
        """
        self.logger.info("EcoScreen 'Start The Machine' button clicked.")  # Log button click
        if self.parent():
            self.parent().setCurrentIndex(1)  # Assuming 1 is the index for the next screen
            self.logger.info("Navigated from EcoScreen to Standby screen.")