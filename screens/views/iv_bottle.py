import logging  #logging module
# Configure logging
logging.basicConfig(level=logging.INFO)  # logging: set logging level to INFO

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnDone

def setup_ui(self):
    logging.info("Initializing main vertical layout")  # logging
    layout = QVBoxLayout()
    hDiv = QHBoxLayout()

    # Welcome label
    topText = QLabel("Insert: 1.5 Bottle")
    topText.setAlignment(Qt.AlignCenter)
    topText.setFont(QFont(self.ff_inter, 35))
    shadow = Drop_Shadow()
    topText.setGraphicsEffect(shadow)
    logging.info("Top label with shadow added: 'Insert: 1.5 Bottle'")  # logging

    # Start button
    self.start_button = BtnDone(parent=self)
    self.start_button.clicked.connect(self._on_click)
    logging.info("Start button initialized and click event connected")  # logging
    
    # render the horizontal division
    hDiv.addStretch()
    hDiv.addWidget(topText)
    hDiv.addStretch()
    hDiv.addWidget(self.start_button, alignment=Qt.AlignCenter)
    hDiv.addStretch()
    logging.info("Horizontal layout (hDiv) populated with label and button")  # logging
    # division below for reminders
    vDiv = QVBoxLayout()
    flavor_text = [
        "• Remove caps from bottles",
        "• Only insert clean and dry bottle",
        "• Do not insert glass, bottles, or cans",
        "• Press “Done” when you are finished",
        "  placing bottles",
    ]
    vDiv.addStretch()
    for i in flavor_text:
        bottomText = QLabel(i)
        bottomText.setFont(QFont(self.ff_poppins, 24))
        bottomText.setFixedHeight(50)
        bottomText.setStyleSheet("margin-left:20px;")
        vDiv.addWidget(bottomText)
        logging.info(f"Reminder label added: '{i}'")  # logging
    vDiv.addStretch()
    logging.info("Vertical layout (vDiv) for reminders constructed")  # logging

    layout.addLayout(hDiv)
    layout.addLayout(vDiv)
    self.setLayout(layout)
    logging.info("UI layout set on widget")  # logging
