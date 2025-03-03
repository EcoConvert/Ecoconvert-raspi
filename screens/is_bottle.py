# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.iv_bottle import setup_ui 
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
        setup_ui(self)
    
    def _on_click(self):
        if self.parent():
            self.parent().setCurrentIndex(4) # go to SUP Screen  
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")
