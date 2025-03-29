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
    