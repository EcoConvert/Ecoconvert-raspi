from .base_screen import BaseScreen
from .views.error_view import setup_ui 

class ErrorScreen(BaseScreen):
    def __init__(self, config, parent=None):
        super().__init__(config, parent)
        setup_ui(self)
        
    def _on_hit(self):
        print("shit may error")