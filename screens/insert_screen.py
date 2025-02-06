from .base_screen import BaseScreen
from .views.insert_view import setup_ui 

class InsertScreen(BaseScreen):
    def __init__(self, config, parent=None):
        super().__init__(config, parent)  # Inherit from BaseScreen
        setup_ui(self)

    def _on_click(self):
        try:
            print("Finish session button clicked")
        
        except Exception as e:
            self.logger.error(
                f"Error navigating to the next screen: {e}", exc_info=True
            )
        
