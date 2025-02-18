from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor
from screens.views._DropShadow import Drop_Shadow

class Btn(QPushButton):
    """
    Creates the generic Button
    """
    def __init__(self, text="click", bt_w = 642, bt_h = 202, padding_size = 10, disabled = False, parent=None):
        super().__init__(parent)
        self.setText("")

        self.label = QLabel(text, self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(parent.font_inter)
        self.label.setStyleSheet(f"padding: {str(padding_size)}px; border: none;")
        shadow = Drop_Shadow()
        self.setGraphicsEffect(shadow)
        
        # change color based on disable
        if disabled: 
            self.setStyleSheet(f"margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")
            self.setEnabled(False)
        else:
            self.setStyleSheet(f"margin-bottom:30px; background-color:#F9FF89; border: 3px solid black; border-radius: 20%")
        self.setFixedSize(bt_w, bt_h)


        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


