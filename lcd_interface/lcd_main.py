import os
import random
import sys

from dotenv import load_dotenv
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

# Add the parent directory to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.Camera import Camera

# Load environment variables from .env file
load_dotenv()


# TODO: Add some details on what's happening with the processing screen
# TODO: Add a QR code image to the completion screen
# TODO: Add .env
# TODO: The application should be scalable and easy to maintain (Dimension)
# FIXME: Fix spacing issue
# FIXME: Fix the error display issue and show the error (what's causing the error)


class RVMInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RVM LCD Interface")
        self.setGeometry(100, 100, 480, 320)

        # Initialize camera
        try:
            self.camera = Camera(camera_id=0)  # Laptop camera: 0, USB camera: 1 or 2
            self.camera.load_labels()
        except Exception as e:
            self.camera = None
            self.show_error_popup(f"Camera initializtion failed: {str(e)}")

        # Load constants from .env file
        self.welcome_message = os.getenv("WELCOME_MESSAGE")
        self.instruction_text = os.getenv("INSTRUCTION_TEXT")
        self.processing_status = os.getenv("PROCESSING_STATUS")
        self.completed_status = os.getenv("COMPLETED_STATUS")
        self.qr_code_message = os.getenv("QR_CODE_MESSAGE")

        # Main layout
        self.layout = QVBoxLayout()

        # Stacked widget for different screens
        self.stacked_widget = QStackedWidget()  # Single page at a time
        self.layout.addWidget(self.stacked_widget)

        # Create screens
        self.create_welcome_screen()  # Index: 0
        self.create_reminder_screen()  # Index: 1
        self.create_processing_screen()  # Index: 2
        self.create_detection_result_screen()  # Index: 3
        self.create_completion_screen()  # Index: 4

        # Set layout
        self.setLayout(
            self.layout
        )  # setLayout handles the layout of the widget automatically

        # Show the welcome screen initially
        self.stacked_widget.setCurrentIndex(0)

        # Store detected results
        self.detection_result = None

        # Define error condtions
        self.error_items = {
            "glass": "Glass materials are not allowed",
            "metal": "Metal materials are not allowed",
            "plastic": "Please use PET bottles only",
            "rock": "Rock/stone materials are not allowed",
            "trash": "General trash is not allowed",
            "Not_1.5": "Please use 1.5L PET bottles only",
            "Crumpled": "Please do not use crumpled bottles",
            "Capped": "Please remove the bottle cap",
            "unclean": "Please clean the bottle first",
            "leaf": "Please remove any leaves or organic materials",
        }

    # ========================== WELCOME SCREEN ========================== #
    def create_welcome_screen(self):
        """Create the initial welcome screen with basic instructions."""
        welcome_widget = QWidget()
        welcome_layout = QVBoxLayout()

        # Set background color for the entire welcome screen widget
        # For Debugging purposes
        # welcome_widget.setStyleSheet(
        # "background-color: lightblue;"
        # )  # Light blue background

        # Welcome label with a different color (optional)
        welcome_label = QLabel("Let's make an Ecobrick!", self)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;"  # Orange Color for background debugging
        )
        welcome_layout.addWidget(welcome_label)

        # Instruction label with a different color
        instruction_label = QLabel(self.instruction_text, self)
        instruction_label.setAlignment(Qt.AlignHCenter)
        instruction_label.setStyleSheet(
            "font-size: 18px; font-weight: bold ; margin-bottom: 50px;"
        )  # Light green background
        welcome_layout.addWidget(instruction_label)

        instructions = [
            "1. Prepare a clean 1.5L PET Bottle and Single-Use Plastic",
            "2. Take off the bottle cap",
            "3. Put the SUP, PET Bottle, and bottle cap in designated slots",
            "4. Wait for the processing to complete",
            "5. Take a picture of the QR Code",
        ]
        for instruction in instructions:
            label = QLabel(instruction, self)
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 16px; margin-left: 5px;")
            welcome_layout.addWidget(label)

        start_button = QPushButton("Next", self)
        start_button.clicked.connect(self.show_instruction_screen)
        start_button.setStyleSheet("font-size: 18px; margin-top: 50px;")
        welcome_layout.addWidget(start_button)

        welcome_widget.setLayout(welcome_layout)
        self.stacked_widget.addWidget(welcome_widget)

    # ========================== WELCOME SCREEN ========================== #

    # ========================== REMINDER SCREEN ========================== #
    def create_reminder_screen(self):
        """Create the detailed instruction screen."""
        reminder_widget = QWidget()
        reminder_layout = QVBoxLayout()

        title = QLabel("Reminders", self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
        reminder_layout.addWidget(title)

        reminders = [
            "• Only insert clean and dry bottles and SUP",
            "• Remove caps from bottles",
            "• Do not insert glass, bottles, or cans",
            "• Do not insert contaminated or wet plastic",
        ]
        for reminder in reminders:
            label = QLabel(reminder, self)
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 16px; margin-left: 20px;")
            reminder_layout.addWidget(label)

        start_button = QPushButton("Start Processing", self)
        start_button.clicked.connect(self.start_processing)
        start_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        reminder_layout.addWidget(start_button)

        reminder_widget.setLayout(reminder_layout)
        self.stacked_widget.addWidget(reminder_widget)

    # ========================== REMINDER SCREEN ========================== #

    # ========================== PROCESSING SCREEN ========================== #
    def create_processing_screen(self):
        """Create the processing screen."""
        processing_widget = QWidget()
        processing_layout = QVBoxLayout()

        self.processing_label = QLabel(self.processing_status, self)
        self.processing_label.setAlignment(Qt.AlignCenter)
        self.processing_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
        )
        processing_layout.addWidget(self.processing_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet("font-size: 16px;")
        processing_layout.addWidget(self.progress_bar)

        processing_widget.setLayout(processing_layout)
        self.stacked_widget.addWidget(processing_widget)

    # ========================== PROCESSING SCREEN ========================== #

    # ========================== DETECTION SCREEN ========================== #

    def check_detection_result(self, result):
        """Check if the detected item is allowed or not.
        Return (is_error, error_message)
        """
        if result is None:
            return True, "No detection results"

        result = str(result).lower()

        # Check if the detected item is in the error items
        for item, error_message in self.error_items.items():
            if item.lower() in result:
                return True, error_message

        # If 1.5L and not crumpled, return False (SUBJECT TO CHANGE)
        if "pet_bottle_1.5l" in result:
            return False, "Valid item"

        # If nothing
        return True, "Unknown item detected"

    def create_detection_result_screen(self):
        """Create a new screen to display detection results."""
        result_widget = QWidget()
        result_layout = QVBoxLayout()

        # Ttile
        result_title = QLabel("Detection Results", self)
        result_title.setAlignment(Qt.AlignCenter)
        result_title.setStyleSheet(
            "font-size: 20px; font-weight: bold; margin-bottom: 15px;"
        )
        result_layout.addWidget(result_title)

        # Result Label (to be updated with detection results)
        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        result_layout.addWidget(self.result_label)

        # Continue button
        continue_button = QPushButton("Continue", self)
        continue_button.clicked.connect(self.show_completion_screen)
        continue_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        result_layout.addWidget(continue_button)

        result_widget.setLayout(result_layout)
        self.stacked_widget.addWidget(result_widget)

    def show_detection_results(self, message=None):
        """Show the detection results on the screen."""
        if not message:
            message = "No detection results"

        # set the result text
        self.result_label.setText(message)

        # Set status style
        status_color = "green" if "Valid" in message else "red"
        self.result_label.setStyleSheet(
            f"font-size: 18px; color: {status_color}; margin-bottom: 20px;"
        )
        # Show the detection result screen
        self.stacked_widget.setCurrentIndex(3)

    # ========================== DETECTION SCREEN ========================== #

    # ========================== COMPLETION SCREEN ========================== #
    def create_completion_screen(self):
        """Create the completion screen with QR code."""
        completion_widget = QWidget()
        completion_layout = QVBoxLayout()

        completion_label = QLabel(self.completed_status, self)
        completion_label.setAlignment(Qt.AlignCenter)
        completion_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
        )
        completion_layout.addWidget(completion_label)

        qr_code_label = QLabel(self.qr_code_message, self)
        qr_code_label.setAlignment(Qt.AlignCenter)
        qr_code_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        completion_layout.addWidget(qr_code_label)

        # Placeholder for QR code image
        qr_placeholder = QLabel("[ QR Code Placeholder ]", self)
        qr_placeholder.setAlignment(Qt.AlignCenter)
        qr_placeholder.setStyleSheet(
            "font-size: 16px; border: 2px solid black; padding: 20px;"
        )
        completion_layout.addWidget(qr_placeholder)

        finish_button = QPushButton("Finish", self)
        finish_button.clicked.connect(self.reset_machine)
        finish_button.setStyleSheet("font-size: 18px; margin-top: 20px;")
        completion_layout.addWidget(finish_button)

        completion_widget.setLayout(completion_layout)
        self.stacked_widget.addWidget(completion_widget)

    # ========================== COMPLETION SCREEN ========================== #

    # FLOW CONTROL METHODS
    def show_instruction_screen(self):
        """Show the detailed instruction screen."""
        self.stacked_widget.setCurrentIndex(1)

    def start_processing(self):
        """Start the processing and detection sequence."""
        if not self.camera:
            self.show_error_popup("Camera not initialized.")
            return

        self.stacked_widget.setCurrentIndex(2)
        self.progress_bar.setValue(0)

        # initialize camera
        try:
            self.camera.init_camera()
        except Exception as e:
            self.show_error_popup(f"Error initializing camera: {str(e)}")
            return

        # Start the processing simulation
        self.simulate_processing_with_detection()

    def simulate_processing_with_detection(self):
        """Simulate the processing with detection."""
        self.progress_bar.setValue(0)

        # Update the processing status
        self.progress_bar.setValue(50)
        self.processing_label.setText("Detecting...")
        QApplication.processEvents()

        try:
            # perform detection
            self.detection_result = self.camera.capture_and_infer()

            # Check if detection was successful
            if self.detection_result is None:
                raise Exception("Detection failed")

            # Check if result is an error condition
            is_error, error_message = self.check_detection_result(self.detection_result)

            # Update the processing status
            self.progress_bar.setValue(100)
            self.processing_label.setText("Scan Completed")
            QApplication.processEvents()

            if is_error:
                self.show_error_popup(error_message)
            else:
                self.show_detection_results(error_message)

        except Exception as e:
            self.show_error_popup(f"Error during detection: {str(e)}")
            self.stacked_widget.setCurrentIndex(1)  # Return to instruction screen
        finally:
            self.camera.release_camera()

    def show_error_popup(self, message):
        """Show an error popup and return to the instruction screen."""
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setText("An error occurred")
        error_msg.setInformativeText(message)
        error_msg.setWindowTitle("Error")
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec_()
        self.stacked_widget.setCurrentIndex(1)  # Return to instruction screen

    def show_completion_screen(self):
        """Show the completion screen with QR code."""
        self.stacked_widget.setCurrentIndex(4)

    def reset_machine(self):
        """Reset the machine state and return to the welcome screen."""
        self.detection_result = None
        self.stacked_widget.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    rvm_interface = RVMInterface()
    rvm_interface.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
