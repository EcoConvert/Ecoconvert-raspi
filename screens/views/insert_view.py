import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

# Configure logging
logging.basicConfig(level=logging.INFO)

def setup_ui(self):
    logging.info("Setting up UI layout")  # logging
    layout = QVBoxLayout()

    insert_label = QLabel("Inserts Mode Screen")
    layout.addWidget(insert_label)
    logging.info("Inserted label widget with text: 'Inserts Mode Screen'")  # logging

    # not finna lie, this shit is like old school jquery, with class abstraction on top. 
    start_button = QPushButton("Finish Session")
    start_button.setStyleSheet("font-size: 18px; margin-top: 30px;")
    start_button.clicked.connect(self._on_click)
    layout.addWidget(start_button)
    logging.info("Added 'Finish Session' button and connected click event")  # logging
    
    self.setLayout(layout)
    logging.info("Layout set on self")  # logging dito logging doon
