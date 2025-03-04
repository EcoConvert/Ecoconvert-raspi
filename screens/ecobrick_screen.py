# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.ecobrick_view import setup_ui 
class EcoScreen(BaseScreen):
    """
    Ecobrick Retrieve screen
    """
    
    def __init__(self, config, parent=None):
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.ecobrick = 0
        setup_ui(self)
    
    def _on_click(self):
        if self.parent():
            self.parent().setCurrentIndex(1)
