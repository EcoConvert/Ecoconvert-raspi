from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import Btn

def setup_ui(self):
        """
        Set up the user interface for the Reminder Screen.
        """
        layout = QVBoxLayout()

        # Title
        title = QLabel("Choose to Insert")
        title.setFont(self.font_poppins)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; margin-bottom: 15px;")
        shadow = Drop_Shadow()
        title.setGraphicsEffect(shadow)
        layout.addWidget(title)


        div = QHBoxLayout()
        bot_btn = Btn("1.5 Plastic <br> Bottle", bt_w = 298, bt_h = 202, padding_size = 0, disabled = True, parent=self)
        div.addWidget(bot_btn)

        sup_btn = Btn("Single Use <br> Plastic", bt_w = 298, bt_h = 202, padding_size = 0, parent=self)
        div.addWidget(sup_btn)

        layout.addLayout(div)
        self.setLayout(layout)
