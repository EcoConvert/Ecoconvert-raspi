# src/lcd_interface/screens/welcome_screen.py
from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_bottle import setup_ui 
from util.state import save_state_variables

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
            self.parent().setCurrentIndex(4) # go to QR Screen
            qr_screen = self.parent().widget(4)
            qr_screen.generate_qr(24)

        else:
            self.logger.warning("No parent QStackedWidget found.")
    
    def process(self): 
        # open the camera here
        print("processing bottle")
        
        valid =  True
        if valid: 
            save_state_variables("bottle_exist", True)
            print("Valid bottle ")
        else:
            pass
