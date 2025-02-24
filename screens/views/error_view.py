from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack

def setup_ui(self):
    hDiv = QHBoxLayout()
    # Welcome label
    #hDiv.addStretch()
    # left side 
    left = QVBoxLayout()
    # heading
    heading = QLabel("Error!😟")
    heading.setAlignment(Qt.AlignCenter)
    heading.setFont(QFont(self.ff_poppins, 50))
    # subhead
    logs = " Ur fault: Do not insert <br> non plastic item.<br> RETRIEVE IT"
    self.subhead = QLabel(f"Logs: {logs}")
    self.subhead.setFont(QFont(self.ff_poppins, 15))
    self.subhead.setAlignment(Qt.AlignCenter)
    # points
    if self.error_code is None:
        self.error_code = 0
    self.error_code_label = QLabel(f"error_code: {self.error_code}")
    self.error_code_label.setFont(QFont(self.ff_poppins, 24))
    self.error_code_label.setAlignment(Qt.AlignCenter)
    # top back button
    back = BtnBack(parent=self)
    back.clicked.connect(self._on_click)
    
    left.addWidget(back)
    left.addWidget(heading)
    left.addWidget(self.subhead)
    left.addWidget(self.error_code_label)
    

    # right side
    right = QVBoxLayout()
    self.qr = QLabel("")
    self.qr.setStyleSheet("background-color: #faefae; border: 3px solid black;")
    self.qr.setFixedSize(374, 374)

    right.addWidget(self.qr)
    hDiv.addLayout(left)
    hDiv.addLayout(right)
    # Set layout
    self.setLayout(hDiv)