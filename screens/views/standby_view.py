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
        self.bot_btn = Btn("1.5 Plastic <br> Bottle", bt_w = 298, bt_h = 202, padding_size = 0, parent=self)
        self.bot_btn.clicked.connect(self._on_click_pet)
        div.addWidget(self.bot_btn)

        self.sup_btn = Btn("Single Use <br> Plastic", bt_w = 298, bt_h = 202, padding_size = 0, parent=self)
        self.sup_btn.clicked.connect(self._on_click_sup)
        div.addWidget(self.sup_btn)

        layout.addLayout(div)
        self.setLayout(layout)
