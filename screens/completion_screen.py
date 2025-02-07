# src/lcd_interface/screens/completion_screen.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from .base_screen import BaseScreen
from .views.completion_view import setup_ui

class CompletionScreen(BaseScreen):
    """
    Completion screen for the RVM LCD Interface.

    Displays a completion message and a QR code placeholder.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the completion screen.

        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)
        setup_ui(self)

    def _on_click(self):
        """
        Handle the 'Finish' button click event.

        Resets the application to the welcome screen.
        """
        if self.parent():
            self.parent().setCurrentIndex(0)  # Welcome Screen Index
            self.logger.info("Reset to Welcome Screen.")
            self.update_state(3)
