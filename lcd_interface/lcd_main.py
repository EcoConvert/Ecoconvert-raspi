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

# Load environment variables from .env file
load_dotenv()


# TODO: Try to implement a loop that switches between welcome screen and reminder screen
# TODO: Add some details on what's happening with the processing screen
# TODO: Add a QR code image to the completion screen
# TODO: Add .env
# TODO: The application should be scalable and easy to maintain
# FIXME: Fix spacing issue
# FIXME: Fix the error display issue and show the error (what's causing the error)


class RVMInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RVM LCD Interface")
        self.setGeometry(100, 100, 480, 320)

        # Load constants from .env file
        self.welcome_message = os.getenv("WELCOME_MESSAGE", "Welcome to the RVM!")
        self.instruction_text = os.getenv("INSTRUCTION_TEXT", "How to use the system:")
        self.processing_status = os.getenv("PROCESSING_STATUS", "Processing")
        self.completed_status = os.getenv("COMPLETED_STATUS", "Completed")
        self.qr_code_message = os.getenv(
            "QR_CODE_MESSAGE", "Take a picture of this QR Code"
        )

        # Main layout
        self.layout = QVBoxLayout()

        # Stacked widget for different screens
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Create screens
        self.create_welcome_screen()
        self.create_reminder_screen()
        self.create_processing_screen()
        self.create_completion_screen()

        # Set layout
        self.setLayout(self.layout)

        # Show the welcome screen initially
        self.stacked_widget.setCurrentIndex(0)

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
        # instruction_label.setFixedHeight(100)
        welcome_layout.addWidget(instruction_label)

        # Instructions list (each instruction could also have a different color if needed)
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
            label.setStyleSheet(
                "font-size: 16px; margin-left: 5px;"
            )  # Light yellow background for each instruction
            welcome_layout.addWidget(label)

        # Start button with a different color
        start_button = QPushButton("Next", self)
        start_button.clicked.connect(self.show_instruction_screen)
        start_button.setStyleSheet(
            "font-size: 18px; margin-top: 50px;"
        )  # Light gray background for the button
        welcome_layout.addWidget(start_button)

        welcome_widget.setLayout(welcome_layout)
        self.stacked_widget.addWidget(welcome_widget)

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

    ### BETA

    # def start_screen_loop(self):
    # """Start the loop to swtich between welcome screen and reminder screen every 2 seconds."""
    # self.current_screen_index = 0

    # # Timer to trigger screen switch every 2 seconds
    # self.timer = QTimer(self)
    # self.timer.timeout.connect(self.switch_screen)
    # self.timer.start(2000)

    # def switch_screen(self):
    # """Switch between the welcome screen and reminder screen."""

    # # Alternate between the welcome screen and reminder screen
    # self.current_screen_index = 1 - self.current_screen_index

    # self.stacked_widget.setCurrentIndex(self.current_screen_index)

    ### BETA

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

    def show_instruction_screen(self):
        """Show the detailed instruction screen."""
        self.stacked_widget.setCurrentIndex(1)

    def start_processing(self):
        """Start the processing simulation."""
        self.stacked_widget.setCurrentIndex(2)
        self.progress_bar.setValue(0)
        self.simulate_processing()

    def simulate_processing(self):
        """Simulate the processing with a chance of error."""
        for i in range(500000):
            self.progress_bar.setValue(i)
            QApplication.processEvents()
            QTimer.singleShot(1000, lambda: None)  # Short delay for visual effect

        # Simulate a 20% chance of error
        if random.random() < 0.2:
            self.show_error_popup()
        else:
            self.show_completion_screen()

    def show_error_popup(self):
        """Show an error popup and return to the instruction screen."""
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setText("An error occurred during processing.")
        error_msg.setInformativeText("Please check your bottles and try again.")
        error_msg.setWindowTitle("Error")
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec_()
        self.stacked_widget.setCurrentIndex(1)  # Return to instruction screen

    def show_completion_screen(self):
        """Show the completion screen with QR code."""
        self.stacked_widget.setCurrentIndex(3)

    def reset_machine(self):
        """Reset the machine state and return to the welcome screen."""
        self.stacked_widget.setCurrentIndex(0)
        # self.start_screen_loop()


def main():
    app = QApplication(sys.argv)
    rvm_interface = RVMInterface()
    rvm_interface.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
