import logging  # logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnDone

def setup_ui(self):
    logging.info("SUP UI: Initializing main vertical layout")  # logging
    layout = QVBoxLayout()
    hDiv = QHBoxLayout()

    # Welcome label
    topText = QLabel("Insert: SUP")
    topText.setAlignment(Qt.AlignCenter)
    topText.setFont(QFont(self.ff_inter, 35))
    shadow = Drop_Shadow()
    topText.setGraphicsEffect(shadow)
    logging.info("SUP UI: Top label with shadow added: 'Insert: SUP'")  # logging

    # Start button
    self.start_button = BtnDone(parent=self)
    self.start_button.clicked.connect(self._on_click)
    logging.info("SUP UI: Start button initialized and click event connected")  # logging

    # render the horizontal division
    hDiv.addStretch()
    hDiv.addWidget(topText)
    hDiv.addStretch()
    hDiv.addWidget(self.start_button, alignment=Qt.AlignCenter)
    hDiv.addStretch()
    logging.info("SUP UI: Horizontal layout (hDiv) populated with label and button")  # logging

    # division below for reminders
    vDiv = QVBoxLayout()
    flavor_text = [
        "• Do not insert contaminated or wet plastic",
        "• Insert clean and dry Single Use Plastic (SUP)",
        "• Press “Done” when you are finished placing",
        "SUP"
    ]
    vDiv.addStretch()
    for i in flavor_text:
        bottomText = QLabel(i)
        bottomText.setFont(QFont(self.ff_poppins, 24))
        bottomText.setFixedHeight(50)
        bottomText.setStyleSheet("margin-left:20px;")
        vDiv.addWidget(bottomText)
        logging.info(f"SUP UI: Reminder label added: '{i}'")  # logging
    vDiv.addStretch()
    logging.info("SUP UI: Vertical layout (vDiv) for reminders constructed")  # logging

    layout.addLayout(hDiv)
    layout.addLayout(vDiv)
    self.setLayout(layout)
    logging.info("SUP UI: Full layout set on widget")  # logging
