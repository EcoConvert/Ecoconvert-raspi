from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

def setup_ui(self):
    layout = QVBoxLayout()
    insert_label = QLabel(
         "Inserts Mode Screen"
    )
    layout.addWidget(insert_label)
    # not finna lie, this shit is like old school jquery, with class abstraction on top. 
    start_button = QPushButton("Finish Session")
    start_button.setStyleSheet("font-size: 18px; margin-top: 30px;")
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button)
    
    self.setLayout(layout)