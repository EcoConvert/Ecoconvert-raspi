# src/lcd_interface/screens/welcome_screen.py
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
    
    def _on_click(self):
        if self.parent():
            self.update_state(0) # update to standby
            standby_screen = self.parent().widget(1)
            # implement conditional showing of button
            standby_screen.global_state_checker() # <-screen changer  is on this one 
        else:
            self.logger.warning("No parent QStackedWidget found.")

    def generate_qr(self, value):
        print("generating qr")  
        self.pointsLabel.setText(f"Points: {value}")
        
