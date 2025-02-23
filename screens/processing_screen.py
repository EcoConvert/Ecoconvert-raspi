# src/lcd_interface/screens/processing_screen.py
import random

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication

from .base_screen import BaseScreen
from .views.processing_view import setup_ui

class ProcessingScreen(BaseScreen):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        self.progress_value = 0  # Current progress value
        setup_ui(self)