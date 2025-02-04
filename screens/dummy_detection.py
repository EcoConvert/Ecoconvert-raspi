# src/lcd_interface/screens/detection_result_screen.py
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from .base_screen import BaseScreen


class DetectionResultScreen(BaseScreen):
    """
    Dummy Detection Result Screen for the RVM LCD Interface.

    Simulates the display of detection results without real object detection.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the dummy detection result screen.

        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)
        self._setup_ui()

    def _setup_ui(self):
        """
        Set up the user interface for the detection result screen.
        """
        layout = QVBoxLayout()

        # Title
        result_title = QLabel("Detection Results")
        result_title.setAlignment(Qt.AlignCenter)
        result_title.setStyleSheet(
            "font-size: 20px; font-weight: bold; margin-bottom: 15px;"
        )
        layout.addWidget(result_title)

        # Result Label
        self.result_label = QLabel("Detecting...")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        layout.addWidget(self.result_label)

        # Continue Button
        continue_button = QPushButton("Continue")
        continue_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        continue_button.clicked.connect(self._on_continue_clicked)
        layout.addWidget(continue_button)

        self.setLayout(layout)

        # Simulate detection result
        self._simulate_detection_result()

    def _simulate_detection_result(self):
        """
        Simulate a dummy detection result after a short delay.
        """
        dummy_results = [
            {"message": "Valid Item: 1.5L PET Bottle", "is_valid": True},
            {"message": "Error: Glass materials are not allowed", "is_valid": False},
            {"message": "Error: Metal materials are not allowed", "is_valid": False},
            {"message": "Valid Item: SUP Plastic Detected", "is_valid": True},
            {"message": "Error: Please clean the bottle first", "is_valid": False},
        ]

        # Randomly select a dummy result
        result = random.choice(dummy_results)

        # Update UI to reflect the result
        self.show_result(result["message"], result["is_valid"])

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
