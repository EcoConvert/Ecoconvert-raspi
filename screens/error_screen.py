from .base_screen import BaseScreen
from .views.error_view import setup_ui
from logging_config import lcd_logger  

class ErrorScreen(BaseScreen):
    def __init__(self, config, parent=None):
        super().__init__(config, parent)
        self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this screen
        self.error_code = -4
        self.logger.debug("Initializing ErrorScreen")  # Log when screen is initialized
        setup_ui(self)
        
    def _on_click(self):
        """
        Handle the click event to navigate to a different screen.
        """
        self.logger.info("Error screen 'Continue' button clicked")  # Log button click
        if self.parent():
            self.parent().setCurrentIndex(1)  # Go to another screen (e.g., Home or Welcome screen)
            self.logger.info("Navigated from Error Screen to Welcome Screen.")
    
    def spawn_error_page(self, error_code, error_message, action_message):
        """
        Spawn the error page with the given error code and message.
        
        Args:
            error_code (int): The error code to display.
            error_message (str): The error message to display.
            action_message (str): The message instructing the user on what action to take.
        """
        self.logger.debug(f"Spawning error page with error code: {error_code}")  # Log spawning error page
        self.error_code = error_code
        self.error_message = error_message
        self.error_code_label.setText(f"Error Code: {str(self.error_code)}")
        self.subhead.setText(self.error_message.upper())
        self.action.setText(action_message)

        # Log error page setup
        self.logger.info(f"Error page set with message: {self.error_message} and action: {action_message}")
