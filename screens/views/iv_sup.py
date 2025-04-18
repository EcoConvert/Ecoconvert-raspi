from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnDone
from logging_config import lcd_logger  

def setup_ui(self):
    self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger
    self.logger.debug("Initializing Insert SUP UI")  # Logging added

    layout = QVBoxLayout()
    hDiv = QHBoxLayout()
    self.logger.debug("Main vertical and horizontal layouts created")  # Logging added

    # Welcome label
    topText = QLabel("Insert: SUP")
    topText.setAlignment(Qt.AlignCenter)
    topText.setFont(QFont(self.ff_inter, 35))
    shadow = Drop_Shadow()
    topText.setGraphicsEffect(shadow)
    self.logger.debug("Top label for SUP and shadow effect applied")  # Logging added

    # Start button
    self.start_button = BtnDone(parent=self)
    self.start_button.clicked.connect(self._on_click)
    self.logger.debug("Start button initialized and connected")  # Logging added

    # Render the horizontal division
    hDiv.addStretch()
    hDiv.addWidget(topText)
    hDiv.addStretch()
    hDiv.addWidget(self.start_button, alignment=Qt.AlignCenter)
    hDiv.addStretch()
    self.logger.debug("Horizontal layout populated")  # Logging added

    # Division below for reminders
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
    vDiv.addStretch()
    self.logger.debug("Reminder labels for SUP created and added")  # Logging added

    layout.addLayout(hDiv)
    layout.addLayout(vDiv)
    self.setLayout(layout)
    self.logger.debug("Final layout set")  # Logging added
