from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack
import logging

def setup_ui(self):
    self.logger.debug("Starting UI setup")  #Logging added
    hDiv = QHBoxLayout()
    self.logger.debug("Created main horizontal layout")  #Logging added
    # Welcome label
    #hDiv.addStretch()
    # left side 
    left = QVBoxLayout()
    self.logger.debug("Created left vertical layout")  #Logging added
    # heading
    heading = QLabel("Get all the<br>completed ecobricks")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))
    self.logger.debug("Heading label initialized")  #Logging added
    # subhead
    # ecobrick
    if self.ecobrick is None:
        self.logger.debug("Ecobrick value is None, setting to 0")  #Logging added
        self.ecobrick = 0
    self.ecobrickLabel = QLabel(f"ecobrick: {self.ecobrick}")
    self.ecobrickLabel.setFont(QFont(self.ff_poppins, 24))
    self.ecobrickLabel.setAlignment(Qt.AlignCenter)
    self.logger.debug(f"Ecobrick label set with value: {self.ecobrick}")  #Logging added
    # top back button
    back = BtnBack(parent=self)
    back.clicked.connect(self._on_click)
    self.logger.debug("Back button initialized and connected")  #Logging added
    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(self.ecobrickLabel)
    self.logger.debug("Widgets added to left layout")  #Logging added
    hDiv.addLayout(left)
    self.logger.debug("Left layout added to main horizontal layout")  #Logging added
    # Set layout
    self.setLayout(hDiv)
    self.logger.debug("Layout set for the widget")  #Logging added