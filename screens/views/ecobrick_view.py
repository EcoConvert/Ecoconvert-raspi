from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnBack

def setup_ui(self):
    # hDiv = QHBoxLayout()
    # # Welcome label
    # #hDiv.addStretch()
    # # left side 
    # left = QVBoxLayout()
    # # heading
    # heading = QLabel("Get all the<br>completed ecobricks")
    # heading.setAlignment(Qt.AlignCenter)
    # heading.setFont(QFont(self.ff_poppins, 50))
    # # subhead
    # # ecobrick
    # if self.ecobrick is None:
    #     self.ecobrick = 0
    # self.ecobrickLabel = QLabel(f"ecobrick: {self.ecobrick}")
    # self.ecobrickLabel.setFont(QFont(self.ff_poppins, 24))
    # self.ecobrickLabel.setAlignment(Qt.AlignCenter)
    # # top back button
    # back = BtnBack(parent=self)
    # back.clicked.connect(self._on_click)
    
    # left.addWidget(back)
    # left.addWidget(heading)
    # left.addWidget(self.ecobrickLabel)
    
    # hDiv.addLayout(left)
    # # Set layout
    # self.setLayout(hDiv)

    main_div = QVBoxLayout()
    # bottle states
    bottle_div = QHBoxLayout()
    main_div.addlayout(bottle_div)
    
    # sup div states
    sup_div = QHBoxLayout()
    main_div.addlayout(sup_div)

    # ecobrick states
    ecobrick_div = QHBoxLayout()
    main_div.addlayout(ecobrick_div)
    

    
    self.setLayout(main_div)