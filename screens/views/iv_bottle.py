from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout,  QTextBrowser
from PyQt5.QtGui import QFont
from screens.views._DropShadow import Drop_Shadow
from screens.views._Button import BtnDone

def setup_ui(self):
    layout = QVBoxLayout()
    hDiv = QHBoxLayout()
    # Welcome label
    #hDiv.addStretch()
    topText = QLabel("Insert: 1.5 Bottle")
    topText.setAlignment(Qt.AlignCenter)
    topText.setFont(QFont(self.ff_inter, 35))
    shadow = Drop_Shadow()
    topText.setGraphicsEffect(shadow)
    #hDiv.addStretch()
    # Start button
    start_button = BtnDone(parent=self)
    start_button.clicked.connect(self._on_click)
    
    # render the horizontal division
    hDiv.addStretch()
    hDiv.addWidget(topText)
    hDiv.addStretch()
    hDiv.addWidget(start_button, alignment=Qt.AlignCenter)
    hDiv.addStretch()

    # division below for reminders
    vDiv = QVBoxLayout()
    flavor_text = [
                "• Remove caps from bottles",
                "• Only insert clean and dry bottle",
                "• Do not insert glass, bottles, or cans",
                "• Press “Done” when you are finished",
                "  placing bottles",]
    vDiv.addStretch()
    for i in flavor_text:
        bottomText = QLabel(i)
        bottomText.setFont(QFont(self.ff_poppins, 24))
        bottomText.setFixedHeight(50)
        bottomText.setStyleSheet("margin-left:20px;")
        vDiv.addWidget(bottomText)
    vDiv.addStretch()

    layout.addLayout(hDiv)
    layout.addLayout(vDiv)
    # Set layout
    self.setLayout(layout)