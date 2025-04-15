import logging  
from .base_screen import BaseScreen
from .views.error_view import setup_ui 

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG)

class ErrorScreen(BaseScreen):
    def __init__(self, config, parent=None):
        super().__init__(config, parent)
        self.error_code = -4
        logging.debug("ErrorScreen initialized with default error_code: %d", self.error_code)  # Logged initialization
        setup_ui(self)
        
    def _on_click(self):
        logging.debug("Button clicked on ErrorScreen")  # Logged button click event
        if self.parent():
            self.parent().setCurrentIndex(1)
    
    def spawn_error_page(self, error_code, error_message, action_message):
        """
        Spawn the error page with the given error code and message.
        """
        self.error_code = error_code
        self.error_message = error_message
        logging.debug("Spawning error page with error_code: %d, error_message: '%s', action_message: '%s'",
                      error_code, error_message, action_message)  # Logged error page spawn details
        self.error_code_label.setText(f"Error Code: {str(self.error_code)}")
        self.subhead.setText(self.error_message.upper())
        self.action.setText(action_message)
