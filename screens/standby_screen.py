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

    def _on_click(self):
        """
        Handle the navigation to the Processing Screen and start processing.
        """
        if self.parent():
            processing_screen = self.parent().widget(2)  # Access Processing Screen
            processing_screen.start_processing()  # Start processing simulation
            self.parent().setCurrentIndex(2)  # Navigate to Processing Screen
            self.logger.info("Navigated from Reminder Screen to Processing Screen")
            self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")
