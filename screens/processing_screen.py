# src/lcd_interface/screens/processing_screen.py
import random

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication

from .base_screen import BaseScreen
from .views.processing_view import setup_ui

class ProcessingScreen(BaseScreen):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        self.timer = QTimer()  # Timer to simulate progress
        self.timer.timeout.connect(self._simulate_progress)
        self.progress_value = 0  # Current progress value
        setup_ui(self)

    def start_processing(self):
        """
        Start the simulated processing sequence.
        """
        self.logger.info("Starting simulated processing...")
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.processing_label.setText("Making Eco BRink cutie pokiee")

        # Start the timer to simulate progress updates
        self.timer.start(100)  # Update every 500ms

    def _simulate_progress(self):
        """
        Simulate progress bar updates and handle detection result.
        """
        if self.progress_value < 100:
            self.progress_value += random.randint(10, 20)  # Increment progress randomly
            if self.progress_value > 100:
                self.progress_value = 100

            self.progress_bar.setValue(self.progress_value)
            QApplication.processEvents()

            if self.progress_value >= 50:
                self.processing_label.setText("Detecting...")

        else:
            # Stop the timer when progress reaches 100%
            self.timer.stop()
            self.processing_label.setText("Scan Completed")
            self.progress_bar.setValue(100)
            QApplication.processEvents()

            # Simulate detection result
            self._simulate_detection_result()

    def _simulate_detection_result(self):
        """
        Simulate dummy detection results and navigate to the next screen.
        """
        dummy_results = [
            {"message": "Valid Item: 1.5L PET Bottle", "is_error": False},
            {"message": "Error: Glass materials are not allowed", "is_error": True},
            {"message": "Error: Metal materials are not allowed", "is_error": True},
            {"message": "Valid Item: SUP Plastic Detected", "is_error": False},
            {"message": "Error: Please clean the bottle first", "is_error": True},
        ]

        result = random.choice(dummy_results)  # Simulate random detection result

        self.logger.info(f"Simulated detection result: {result['message']}")

        if self.parent():
            # Navigate to Detection Result Screen (index 3)
            detection_screen = self.parent().widget(
                3
            )  # Assuming index 3 is DetectionResultScreen
            detection_screen.show_result(result["message"], not result["is_error"])
            self.parent().setCurrentIndex(3)
            self.update_state(2)