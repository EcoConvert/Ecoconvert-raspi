from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QProgressBar, QApplication

def setup_ui(self):
    """
    Set up the user interface for the processing screen.
    """
    layout = QVBoxLayout()

    # Processing label
    self.processing_label = QLabel("Making Ecobrick Cutie!")
    self.processing_label.setAlignment(Qt.AlignCenter)
    self.processing_label.setStyleSheet(
        "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
    )
    layout.addWidget(self.processing_label)

    # Progress bar
    self.progress_bar = QProgressBar()
    self.progress_bar.setValue(0)
    self.progress_bar.setStyleSheet("font-size: 16px;")
    layout.addWidget(self.progress_bar)
    self.setLayout(layout)