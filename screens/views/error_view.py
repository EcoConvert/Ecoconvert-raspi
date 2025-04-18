from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack
from logging_config import lcd_logger  

def setup_ui(self):
    self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this module
    self.logger.debug("Initializing error screen UI")  # Logging added

    bg = QFrame(self)
    bg.setGeometry(0, 0, self.config["window_width"], self.config["window_height"])  # x, y, width, height
    bg.setStyleSheet("background-color: #FF0077;")
    self.logger.debug("Background frame configured")  # Logging added

    hDiv = QHBoxLayout()
    self.logger.debug("Main horizontal layout created")  # Logging added

    # left side 
    left = QVBoxLayout()
    self.logger.debug("Left vertical layout created")  # Logging added

    heading = QLabel("Error!😟")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))
    heading.setStyleSheet("color: white;")
    self.logger.debug("Heading label set")  # Logging added

    self.error_message = "Non 1.5 platic<br>bottle detected!"
    self.subhead = QLabel(f"Error Message: {self.error_message}")
    self.subhead.setFont(QFont(self.ff_poppins, 15))
    self.subhead.setAlignment(Qt.AlignCenter)
    self.subhead.setStyleSheet("color: white;")
    self.logger.debug(f"Subheading set with message: {self.error_message}")  # Logging added

    self.error_code = 0
    self.error_code_label = QLabel(f"error_code: {self.error_code}")
    self.error_code_label.setFont(QFont(self.ff_poppins, 24))
    self.error_code_label.setAlignment(Qt.AlignCenter)
    self.error_code_label.setStyleSheet("color: white;")
    self.logger.debug(f"Error code label set with code: {self.error_code}")  # Logging added

    back = BtnBack(parent=self)
    back.setStyleSheet("color: white; background-color: #FF0077; border: none")
    back.clicked.connect(self._on_click)
    self.logger.debug("Back button initialized and connected")  # Logging added

    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(self.subhead)
    left.addWidget(self.error_code_label)
    self.logger.debug("Widgets added to left layout")  # Logging added

    # right side
    right = QVBoxLayout()
    self.rightHead = QLabel("Action:")
    self.rightHead.setStyleSheet("color: white; font-weight: bold;")
    self.rightHead.setFont(QFont(self.ff_poppins, 24))

    self.action = QLabel("Please retrieve the non 1.5<br>bottle then press return to standby")
    self.action.setStyleSheet("color: white;")
    self.action.setFont(QFont(self.ff_poppins, 15))
    self.action.setAlignment(Qt.AlignTop)

    right.addWidget(self.rightHead)
    right.addWidget(self.action)
    self.logger.debug("Widgets added to right layout")  # Logging added

    hDiv.addLayout(left)
    hDiv.addLayout(right)
    self.logger.debug("Left and right layouts added to main layout")  # Logging added

    self.setLayout(hDiv)
    self.logger.debug("Layout set for the widget")  # Logging added
