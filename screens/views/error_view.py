from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack

def setup_ui(self):
    bg = QFrame(self)
    bg.setGeometry(0, 0, self.config["window_width"]+150, self.config["window_height"]+50)  # x, y, width, height
    bg.setStyleSheet("background-color: #FF0077;")

    hDiv = QHBoxLayout()

    # Welcome label
    #hDiv.addStretch()
    # left side 
    left = QVBoxLayout()
    # heading 
    heading = QLabel("Error!😟")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))
    heading.setStyleSheet("color: white;")
    # subhead
    self.error_message = "Non 1.5 platic<br>bottle detected!"
    self.subhead = QLabel(f"Error Message: {self.error_message}")
    self.subhead.setFont(QFont(self.ff_poppins, 15))
    self.subhead.setAlignment(Qt.AlignCenter)
    self.subhead.setStyleSheet("color: white;")
    # code
    self.error_code = 0
    self.error_code_label = QLabel(f"error_code: {self.error_code}")
    self.error_code_label.setFont(QFont(self.ff_poppins, 24))
    self.error_code_label.setAlignment(Qt.AlignCenter)
    self.error_code_label.setStyleSheet("color: white;")
    # top back button
    back = BtnBack(parent=self)
    back.setStyleSheet("color: white; background-color: #FF0077; border: none")
    back.clicked.connect(self._on_click)
    
    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(self.subhead)
    left.addWidget(self.error_code_label)
    

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
    hDiv.addLayout(left)
    hDiv.addLayout(right)
    # Set layout
    self.setLayout(hDiv)