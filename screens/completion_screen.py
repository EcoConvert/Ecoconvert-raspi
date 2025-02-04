# src/lcd_interface/screens/completion_screen.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from .base_screen import BaseScreen


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
        self._setup_ui()
     

    def _setup_ui(self):
        layout = QVBoxLayout()

        # Completion Message
        completion_label = QLabel(
            self.config.get("completed_status", "Operation completed successfully!")
        )
        completion_label.setAlignment(Qt.AlignCenter)
        completion_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
        )
        layout.addWidget(completion_label)

        # QR Code Placeholder
        qr_code_label = QLabel(
            self.config.get("qr_code_message", "Scan the QR Code below.")
        )
        qr_code_label.setAlignment(Qt.AlignCenter)
        qr_code_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        layout.addWidget(qr_code_label)

        qr_placeholder = QLabel("[QR Code Placeholder]")
        qr_placeholder.setAlignment(Qt.AlignCenter)
        qr_placeholder.setStyleSheet(
            "font-size: 16px; border: 2px solid black; padding: 20px;"
        )
        layout.addWidget(qr_placeholder)

        # Finish Button
        finish_button = QPushButton("Finish")
        finish_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        finish_button.clicked.connect(self._on_finish_clicked)
        layout.addWidget(finish_button)

        self.setLayout(layout)

    def _on_finish_clicked(self):
        """
        Handle the 'Finish' button click event.

        Resets the application to the welcome screen.
        """
        if self.parent():
            self.parent().setCurrentIndex(0)  # Welcome Screen Index
            self.logger.info("Reset to Welcome Screen.")
            self.update_state(3)
