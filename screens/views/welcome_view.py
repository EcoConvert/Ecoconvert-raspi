from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

def setup_ui(self):
    layout = QVBoxLayout()
    # Welcome label
    welcome_label = QLabel(
        self.config.get("welcome_message", "Let's make an Ecobrick!")
    )
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_label.setStyleSheet(
        "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
    )
    layout.addWidget(welcome_label)

    # Instruction label
    instruction_label = QLabel(
        self.config.get("instruction_text", "Follow these steps:")
    )
    instruction_label.setAlignment(Qt.AlignCenter)
    instruction_label.setStyleSheet(
        "font-size: 18px; font-weight: bold; margin-bottom: 50px;"
    )
    layout.addWidget(instruction_label)

    # Detailed instructions
    instructions = self.config.get(
        "detailed_instructions",
        [
            "1. Prepare a clean 1.5L PET Bottle and Single-Use Plastic.",
            "2. Take off the bottle cap.",
            "3. Put the SUP, PET Bottle, and bottle cap in designated slots.",
            "4. Wait for the processing to complete.",
            "5. Take a picture of the QR Code.",
        ],
    )
    for instruction in instructions:
        label = QLabel(instruction)
        label.setAlignment(Qt.AlignLeft)
        label.setStyleSheet(
            "font-size: 16px; margin-left: 10px; margin-bottom: 5px;"
        )
        layout.addWidget(label)

    # Start button
    start_button = QPushButton("Next")
    start_button.setStyleSheet("font-size: 18px; margin-top: 30px;")
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button)

    # Set layout
    self.setLayout(layout)