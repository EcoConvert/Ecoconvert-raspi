import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QTextBrowser
from PyQt5.QtGui import QFont, QPixmap
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack
from logging_config import lcd_logger  

def setup_ui(self):
    self.logger = lcd_logger(self.__class__.__name__)  # Logger setup
    self.logger.debug("Initializing QR Screen UI")  # Logging start

    hDiv = QHBoxLayout()

    # Left side
    left = QVBoxLayout()
    heading = QLabel("Thank you<br>for recycling")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))

    subhead = QLabel("Take a picture of the QR then show it<br>to the assigned marshal.")
    subhead.setFont(QFont(self.ff_poppins, 15))
    subhead.setAlignment(Qt.AlignCenter)

    if self.points is None:
        self.points = 0
    self.pointsLabel = QLabel(f"Points: {self.points}")
    self.pointsLabel.setFont(QFont(self.ff_poppins, 24))
    self.pointsLabel.setAlignment(Qt.AlignCenter)

    back = BtnBack(parent=self)
    back.clicked.connect(self._on_click)

    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(subhead)
    left.addWidget(self.pointsLabel)

    self.logger.debug(f"UI Left side setup with points = {self.points}")  # Logging left side info

    # Right side
    right = QVBoxLayout()
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, "../qr_img/DAHYUN.png")

    self.logger.debug(f"QR image path resolved: {image_path}")  # Logging image path

    self.pixmap = QPixmap(image_path)
    self.qr = QLabel("")
    self.qr.setPixmap(self.pixmap)
    self.qr.setScaledContents(True)
    self.qr.setStyleSheet("border: 3px solid black;")
    self.qr.setFixedSize(374, 374)

    right.addWidget(self.qr)
    self.logger.debug("QR code image loaded and added to UI")  # Logging image load

    hDiv.addLayout(left)
    hDiv.addLayout(right)
    self.setLayout(hDiv)
    self.logger.debug("Final layout set for QR screen")  # Final layout log
