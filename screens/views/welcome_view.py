from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from screens.views._Button import Btn
from screens.views._DropShadow import Drop_Shadow


def setup_ui(self):
    layout = QVBoxLayout()
    # Welcome label
    welcome_label = QLabel("EcoConvert")
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_label.setFont(self.font_poppins)
    shadow = Drop_Shadow()
    welcome_label.setGraphicsEffect(shadow)
    layout.addWidget(welcome_label)

    # Buttons layout
    buttons_layout = QHBoxLayout()
    # Start button
    start_button = Btn("Start The Machine", bt_w = 375 , bt_h = 202, font_size=40, padding_size=0, parent=self)
    start_button.clicked.connect(self._on_click)
    buttons_layout.addWidget(start_button )

    # Add Admin Dashboard button
    admin_button = Btn("Admin", bt_w = 375 , bt_h = 202, font_size=40, padding_size=0, parent=self)
    admin_button.clicked.connect(self._on_click_admin)
    buttons_layout.addWidget(admin_button)

    # ADd horizontal layout
    layout.addLayout(buttons_layout)

    # Set layout
    self.setLayout(layout)