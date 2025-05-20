
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout

from screens.views._Button import Btn
from screens.views._DropShadow import Drop_Shadow


def setup_ui(self):
    layout = QVBoxLayout()

    self.password_label = QLabel("Enter Admin Password:")
    self.password_label.setAlignment(Qt.AlignCenter)
    self.password_label.setFont(self.font_poppins)
    shadow = Drop_Shadow()
    self.password_label.setGraphicsEffect(shadow)
    layout.addWidget(self.password_label)

    # Input password
    self.password_input = QLineEdit()
    self.password_input.setEchoMode(QLineEdit.Password)
    layout.addWidget(self.password_input)

    self.submit_btn = QPushButton("Submit")
    layout.addWidget(self.submit_btn)
    
    self.setLayout(layout)