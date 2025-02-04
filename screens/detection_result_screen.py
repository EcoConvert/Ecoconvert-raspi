# src/lcd_interface/screens/detection_result_screen.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from .base_screen import BaseScreen


class DetectionResultScreen(BaseScreen):
    """
    Detection result screen for the RVM LCD Interface.

    Displays the results of the detection process.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the detection result screen.

        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        # Title
        result_title = QLabel("Detection Results")
        result_title.setAlignment(Qt.AlignCenter)
        result_title.setStyleSheet(
            "font-size: 20px; font-weight: bold; margin-bottom: 15px;"
        )
        layout.addWidget(result_title)

        # Result Label
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        layout.addWidget(self.result_label)

        # Continue Button
        continue_button = QPushButton("Continue")
        continue_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        continue_button.clicked.connect(self._on_continue_clicked)
        layout.addWidget(continue_button)

        self.setLayout(layout)

    def show_result(self, message, is_valid):
        """
        Display the detection result.

        Args:
            message (str): Message to display.
            is_valid (bool): Whether the result is valid or an error.
        """
        color = "green" if is_valid else "red"
        self.result_label.setText(message)
        self.result_label.setStyleSheet(
            f"font-size: 18px; color: {color}; margin-bottom: 20px;"
        )

    def _on_continue_clicked(self):
        """
        Handle the 'Continue' button click event.

        Navigate to the completion screen.
        """
        if self.parent():
            self.parent().setCurrentIndex(4)  # Completion Screen Index
            self.logger.info(
                "Navigated from Detection Result Screen to Completion Screen."
            )
