from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QProgressBar, QApplication
from screens.views._DropShadow import Drop_Shadow
from logging_config import lcd_logger  

def setup_ui(self):
    """
    Set up the user interface for the processing screen.
    """
    self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger
    self.logger.debug("Initializing Processing Screen UI")  # Logging added

    layout = QVBoxLayout()

    # Processing label
    self.processing_label = QLabel("Processing ")
    self.processing_label.setAlignment(Qt.AlignCenter)
    self.processing_label.setFont(self.font_poppins)
    self.processing_label.setStyleSheet("margin-bottom: 20px;")
    shadow = Drop_Shadow()
    self.processing_label.setGraphicsEffect(shadow)
    layout.addWidget(self.processing_label)
    self.logger.debug("Processing label with drop shadow added")  # Logging added

    # Progress bar
    self.progress_bar = QProgressBar()
    self.progress_bar.setValue(0)
    self.progress_bar.setFont(self.font_inter)
    self.progress_bar.setStyleSheet("background-color: black; font-size: 16px;")
    layout.addWidget(self.progress_bar)
    self.logger.debug("Progress bar initialized and added to layout")  # Logging added

    self.setLayout(layout)
    self.logger.debug("Final layout set")  # Logging added
