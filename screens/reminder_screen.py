# src/lcd_interface/screens/reminder_screen.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from .base_screen import BaseScreen


class ReminderScreen(BaseScreen):
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
        self._setup_ui()

    def _setup_ui(self):
        """
        Set up the user interface for the Reminder Screen.
        """
        layout = QVBoxLayout()

        # Title
        title = QLabel("Reminders")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(title)

        # Reminder instructions
        reminders = self.config.get(
            "reminder_text",
            [
                "• Only insert clean and dry bottles and SUP.",
                "• Remove caps from bottles.",
                "• Do not insert glass, bottles, or cans.",
                "• Do not insert contaminated or wet plastic.",
            ],
        )
        for reminder in reminders:
            label = QLabel(reminder)
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 16px; margin-left: 20px;")
            layout.addWidget(label)

        # Start button
        start_button = QPushButton("Start Processing")
        start_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        start_button.clicked.connect(self._navigate_to_processing)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def _navigate_to_processing(self):
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
