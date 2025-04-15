import logging  
# Configure logging
logging.basicConfig(level=logging.INFO)  

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import Btn

def setup_ui(self):
    layout = QVBoxLayout()
    logging.info("Main vertical layout initialized")  # logging

    # Welcome label
    welcome_label = QLabel("EcoConvert")
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_label.setFont(self.font_poppins)
    shadow = Drop_Shadow()
    welcome_label.setGraphicsEffect(shadow)
    layout.addWidget(welcome_label)
    logging.info("Welcome label 'EcoConvert' initialized and added to layout")  # logging

    # Start button
    start_button = Btn("Start The Machine", bt_w = 642 , bt_h = 202, font_size=50, padding_size=0, parent=self)
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button, alignment=Qt.AlignCenter)
    logging.info("Start button initialized and click event connected")  # logging

    # Set layout
    self.setLayout(layout)
    logging.info("Layout applied to widget")  # logging
