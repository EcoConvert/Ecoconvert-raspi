from .base_screen import BaseScreen
from .views.welcome_view import setup_ui
from logging_config import lcd_logger  

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
        
        # Setup the UI
        setup_ui(self)
        
        # Logger initialization
        self.logger = lcd_logger(__name__)  # Initialize logger for WelcomeScreen
        self.logger.debug("Welcome Screen initialized.")  # Log initialization of the screen
        
        # Update state to standby mode
        self.update_state(0)  # update to standby mode
        self.logger.info("State updated to standby mode.")  # Log state update
    
    def _on_click(self):
        """
        Handle the 'Next' button click event.
        """
        try:
            if self.parent():
                # Navigate to the next screen (index 1 assumed) - Standby Screen
                standby_screen = self.parent().widget(1)
                standby_screen.global_state_checker()  # Call global state checker
                self.logger.info("Navigated from Welcome Screen to Standby Screen.")
            else:
                self.logger.warning("No parent QStackedWidget found for navigation.")
        except Exception as e:
            self.logger.error(
                f"Error navigating to the next screen: {e}", exc_info=True
            )