from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import Btn
from logging_config import lcd_logger 

def setup_ui(self):
    self.logger = lcd_logger(self.__class__.__name__)  # Logger setup
    self.logger.debug("Initializing Intro Screen UI")  # Logging UI init

    layout = QVBoxLayout()

    # Welcome label
    welcome_label = QLabel("EcoConvert")
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_label.setFont(self.font_poppins)
    shadow = Drop_Shadow()
    welcome_label.setGraphicsEffect(shadow)
    layout.addWidget(welcome_label)
    self.logger.debug("Welcome label set: 'EcoConvert'")

    # Start button
    start_button = Btn("Start The Machine", bt_w=642, bt_h=202, font_size=50, padding_size=0, parent=self)
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button, alignment=Qt.AlignCenter)
    self.logger.debug("Start button added and connected")

    # Set layout
    self.setLayout(layout)
    self.logger.debug("Intro screen layout applied")
