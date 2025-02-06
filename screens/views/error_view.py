from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

def setup_ui(self):
    layout = QVBoxLayout()
    err_Title = QLabel(
         "Error Error Error"
    )
    layout.addWidget(err_Title) #---
    err_content = QLabel("Please Call the developers immidiately") # update this with things like. JAM, IMPROPER plastic INPUT, UNCLEAN BOTTLE, but not now
    layout.addWidget(err_content)  
    
    self.setLayout(layout)