# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.ecobrick_view import setup_ui 
class EcoScreen(BaseScreen):
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
        self.ecobrick = 0
        setup_ui(self)
    
    def _on_click(self):
        """
        Handle the 'Next' button click event.
        """
        print("back clicking")