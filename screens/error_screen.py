from .base_screen import BaseScreen
from .views.error_view import setup_ui 

class ErrorScreen(BaseScreen):
    def __init__(self, config, parent=None):
        super().__init__(config, parent)
        self.error_code = -4
        setup_ui(self)
        
    def _on_click(self):
        if self.parent():
            self.parent().setCurrentIndex(1)
    

    def spawn_error_page(self, error_code, error_message, action_message):
        """
        Spawn the error page with the given error code and message.
        """
        self.error_code = error_code
        self.error_message = error_message
        self.error_code_label.setText(f"Error Code: {str(self.error_code)}")
        self.subhead.setText(self.error_message.upper())
        self.action.setText(action_message)