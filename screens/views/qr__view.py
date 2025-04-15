import os
import logging 
# Configure logging
logging.basicConfig(level=logging.INFO)  

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QTextBrowser
from PyQt5.QtGui import QFont, QPixmap
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack

def setup_ui(self):
    logging.info("Thank you screen UI: Initializing horizontal layout")  # logging
    hDiv = QHBoxLayout()

    # left side
    left = QVBoxLayout()

    # heading
    heading = QLabel("Thank you<br>for recycling")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))

    # subhead
    subhead = QLabel("Take a picture of the QR then show it<br>to the assigned marshal.")
    subhead.setFont(QFont(self.ff_poppins, 15))
    subhead.setAlignment(Qt.AlignCenter)

    # points
    if self.points is None:
        self.points = 0
    self.pointsLabel = QLabel(f"Points: {self.points}")
    self.pointsLabel.setFont(QFont(self.ff_poppins, 24))
    self.pointsLabel.setAlignment(Qt.AlignCenter)

    logging.info(f"Thank you screen UI: Points label initialized with {self.points} points")  # logging: points label

    # top back button
    back = BtnBack(parent=self)
    back.clicked.connect(self._on_click)
    logging.info("Thank you screen UI: Back button initialized and connected")  # logging: back button

    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(subhead)
    left.addWidget(self.pointsLabel)

    # right side
    right = QVBoxLayout()
    base_path = os.path.dirname(__file__)  # Gets the current module's directory
    image_path = os.path.join(base_path, "../qr_img/DAHYUN.png")
    self.pixmap = QPixmap(image_path)
    self.qr = QLabel("")
    self.qr.setPixmap(self.pixmap)
    self.qr.setScaledContents(True)
    self.qr.setStyleSheet(" border: 3px solid black;")
    self.qr.setFixedSize(374, 374)

    logging.info(f"Thank you screen UI: QR image loaded from {image_path}")  # logging: qr image path

    right.addWidget(self.qr)

    hDiv.addLayout(left)
    hDiv.addLayout(right)
    self.setLayout(hDiv)
    logging.info("Thank you screen UI: Layout set on widget")  # logging: final layout
