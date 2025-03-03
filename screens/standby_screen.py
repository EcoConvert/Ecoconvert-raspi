# src/lcd_interface/screens/reminder_screen.py
from .base_screen import BaseScreen
from .views.standby_view import setup_ui
class StandbyScreen(BaseScreen):
    """
    Reminder screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the Reminder Screen.

        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)
        setup_ui(self)

    def _on_click_pet(self):
        if self.parent():
            self.parent().setCurrentIndex(2) # go to PET Screen  
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")


    def _on_click_sup(self):
        if self.parent():
            self.parent().setCurrentIndex(3) # go to SUP Screen  
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")
    
    def sup_clickability(self, state = True):
        self.sup_button.setEnabled(state)