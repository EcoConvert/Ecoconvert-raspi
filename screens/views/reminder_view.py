from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
def setup_ui(self):
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
        start_button.clicked.connect(self._on_click)
        layout.addWidget(start_button)

        self.setLayout(layout)
