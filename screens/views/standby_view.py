from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import Btn
from logging_config import lcd_logger  
def setup_ui(self):
    """
    Set up the user interface for the Reminder Screen.
    """
    self.logger = lcd_logger(self.__class__.__name__)  # Logger setup
    self.logger.debug("Initializing Reminder Screen UI")  # Logging UI init

    layout = QVBoxLayout()

    # Title
    title = QLabel("Choose to Insert")
    title.setFont(self.font_poppins)
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("font-size: 50px; margin-bottom: 15px;")
    shadow = Drop_Shadow()
    title.setGraphicsEffect(shadow)
    layout.addWidget(title)

    self.logger.debug("Title label configured")

    div = QHBoxLayout()

    self.pet_btn = Btn("1.5 Plastic <br> Bottle", bt_w=298, bt_h=202, padding_size=0, parent=self)
    self.pet_btn.clicked.connect(self._on_click_pet)
    div.addWidget(self.pet_btn)
    self.logger.debug("PET button created and connected")

    self.sup_btn = Btn("Single Use <br> Plastic", bt_w=298, bt_h=202, padding_size=0, parent=self)
    self.sup_btn.clicked.connect(self._on_click_sup)
    div.addWidget(self.sup_btn)
    self.logger.debug("SUP button created and connected")

    layout.addLayout(div)
    self.setLayout(layout)
    self.logger.debug("Final layout set for Reminder Screen")
