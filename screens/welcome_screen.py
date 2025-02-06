# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.welcome_view import setup_ui 
class WelcomeScreen(BaseScreen):
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
        #self._setup_ui()
        
        # this is the new updated way to set up UI. it is divergent from the Object oriented programming because I personally find functional programming more straightforward
        # from self._setup_ui() delete the move the self as parameter, then delete the underscore
        # then hook it up on the views.   
        setup_ui(self)
        self.update_state(0) # update to standby mode

    def _on_click(self):
        """
        Handle the 'Next' button click event.
        """
        try:
            if self.parent():
                # Navigate to the next screen (index 1 assumed)
                self.parent().setCurrentIndex(1)
                self.logger.info("Navigated from Welcome Screen to Reminder Screen.")
                self.update_state(0)
            else:
                self.logger.warning("No parent QStackedWidget found for navigation.")
        except Exception as e:
            self.logger.error(
                f"Error navigating to the next screen: {e}", exc_info=True
            )
        