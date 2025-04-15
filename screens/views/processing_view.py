import logging  # logging: imported logging module

# Configure logging
logging.basicConfig(level=logging.INFO)  # logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QProgressBar, QApplication
from screens.views._DropShadow import Drop_Shadow

def setup_ui(self):
    """
    Set up the user interface for the processing screen.
    """
    logging.info("Processing UI: Initializing vertical layout")  # logging
    layout = QVBoxLayout()

    # Processing label
    self.processing_label = QLabel("Processing ")
    self.processing_label.setAlignment(Qt.AlignCenter)
    self.processing_label.setFont(self.font_poppins)
    self.processing_label.setStyleSheet("margin-bottom: 20px;")
    shadow = Drop_Shadow()  
    self.processing_label.setGraphicsEffect(shadow)
    layout.addWidget(self.processing_label)
    logging.info("Processing UI: Processing label with shadow added")  # logging

    # Progress bar
    self.progress_bar = QProgressBar()
    self.progress_bar.setValue(0)
    self.progress_bar.setFont(self.font_inter)
    self.progress_bar.setStyleSheet("background-color: black; font-size: 16px;")
    layout.addWidget(self.progress_bar)
    logging.info("Processing UI: Progress bar initialized and added to layout")  # logging

    self.setLayout(layout)
    logging.info("Processing UI: Layout set on widget")  # logging
