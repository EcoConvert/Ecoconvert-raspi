from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QProgressBar

def setup_ui(self):
    """
    Set up the user interface for the processing screen.
    """
    layout = QVBoxLayout()

    # Processing label
    title = QLabel("Making Ecobrick Cutie!")
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet(
        "font-size: 24px; font-weight: bold; margin-bottom: 20px;"
    )
    layout.addWidget(title)

    # Progress bar
    pbar = QProgressBar()
    pbar.setValue(0)
    pbar.setStyleSheet("font-size: 16px;")
    layout.addWidget(pbar)
    self.setLayout(layout)