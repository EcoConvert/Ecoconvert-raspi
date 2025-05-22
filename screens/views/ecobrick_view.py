from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack
from screens.views._Button import BtnAdmin


def setup_ui(self):
    main_div = QVBoxLayout()
    # back buttons
    back = BtnBack(parent=self)
    back.clicked.connect(self._on_click_home)
    main_div.addWidget(back)
    
    # bottle states
    bottle_div = QHBoxLayout()
    bottle = QLabel("Bottle")
    bottle.setAlignment( Qt.AlignCenter)
    bottle.setFont(QFont(self.ff_poppins, 35))
    self.is_bottle_existent_label = QLabel("___")
    self.is_bottle_existent_label.setAlignment( Qt.AlignCenter)
    self.pet_toggle = BtnAdmin("toggle", bt_w = 207, bt_h = 93, padding_size = 0, parent=self)
    self.pet_toggle.clicked.connect(self._on_click_pet_toggle)
    bottle_div.addStretch()
    bottle_div.addWidget(bottle)
    bottle_div.addStretch()
    bottle_div.addWidget(self.is_bottle_existent_label)
    bottle_div.addStretch()
    bottle_div.addWidget(self.pet_toggle)
    bottle_div.addStretch()
    main_div.addLayout(bottle_div,  Qt.AlignHCenter)
    
    # sup div states
    sup_div = QHBoxLayout()
    sup = QLabel("SUP")
    sup.setAlignment( Qt.AlignCenter)
    sup.setFont(QFont(self.ff_poppins, 35))
    self.sup_count_label = QLabel("___")
    self.sup_count_label.setAlignment( Qt.AlignCenter)
    # zero button
    self.sup_zero_btn = BtnAdmin("ZERO", bt_w = 116, bt_h = 93, padding_size = 0, parent=self)
    self.sup_zero_btn.clicked.connect(self._on_click_sup_zero)
    # full button
    self.sup_full_btn = BtnAdmin("FULL", bt_w = 116, bt_h = 93, padding_size = 0, parent=self)
    self.sup_full_btn.clicked.connect(self._on_click_sup_full)
    sup_div.addStretch()
    sup_div.addWidget(sup)
    sup_div.addStretch()
    sup_div.addWidget(self.sup_count_label)
    sup_div.addStretch()
    sup_div.addWidget(self.sup_zero_btn)
    sup_div.addWidget(self.sup_full_btn)
    sup_div.addStretch()
    main_div.addLayout(sup_div)

    # ecobrick states
    ecobrick_div = QHBoxLayout()
    ecobrick = QLabel("Stored ecobrick")
    ecobrick.setAlignment(Qt.AlignCenter)
    ecobrick.setFont(QFont(self.ff_poppins, 20))
    self.ecoB_stored_label = QLabel("___")
    self.ecoB_stored_label.setAlignment( Qt.AlignCenter)
    self.brick_reset = BtnAdmin("reset", bt_w = 207, bt_h = 93, padding_size = 0, parent=self)
    self.brick_reset.clicked.connect(self._on_click_ecobrick_reset)
    ecobrick_div.addStretch()
    ecobrick_div.addWidget(ecobrick)
    ecobrick_div.addStretch()
    ecobrick_div.addWidget(self.ecoB_stored_label)
    ecobrick_div.addStretch()
    ecobrick_div.addWidget(self.brick_reset)
    ecobrick_div.addStretch()
    main_div.addLayout(ecobrick_div)
   
    self.setLayout(main_div)
    