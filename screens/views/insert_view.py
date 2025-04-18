from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from logging_config import lcd_logger 

def setup_ui(self):
    self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this module
    self.logger.debug("Initializing Inserts Mode UI")  # Logging added

    layout = QVBoxLayout()
    self.logger.debug("Main vertical layout created")  # Logging added

    insert_label = QLabel("Inserts Mode Screen")
    layout.addWidget(insert_label)
    self.logger.debug("Insert label added to layout")  # Logging added

    # not finna lie, this shit is like old school jquery, with class abstraction on top. 
    start_button = QPushButton("Finish Session")
    start_button.setStyleSheet("font-size: 18px; margin-top: 30px;")
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button)
    self.logger.debug("Finish session button initialized and added")  # Logging added

    self.setLayout(layout)
    self.logger.debug("Layout set for the widget")  # Logging added
