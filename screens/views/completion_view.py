from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

def setup_ui(self):
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
    finish_button.clicked.connect(self._on_click)
    layout.addWidget(finish_button)

    self.setLayout(layout)
