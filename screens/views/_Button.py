from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor, QFont
from screens.views._DropShadow import Drop_Shadow

class Btn(QPushButton):
    """
    Creates the generic Button
    """
    def __init__(self, text="click", bt_w = 642, bt_h = 202, padding_size = 10, font_size = 35, disabled = False, parent=None):
        super().__init__(parent)
        self.label = QLabel(text, self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(parent.ff_inter, font_size)) 
        self.label.setStyleSheet(f"padding: {str(padding_size)}px; border: none;")
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)  
        shadow = Drop_Shadow()
        self.setGraphicsEffect(shadow)
        
        # change color based on disable
        if disabled: 
            self.setStyleSheet("margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")
            self.setEnabled(False)
        else:
            self.setStyleSheet("margin-bottom:30px; background-color:#F9FF89; border: 3px solid black; border-radius: 20%")
            self.setEnabled(True)
        self.setFixedSize(bt_w, bt_h)


        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class BtnAdmin(QPushButton):
    """
    Creates the generic Button
    """
    def __init__(self, text="click", bt_w = 642, bt_h = 202, padding_size = 10, font_size = 20, disabled = False, parent=None):
        super().__init__(parent)
        self.label = QLabel(text, self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(parent.ff_inter, font_size)) 
        self.label.setStyleSheet(f"padding: {str(padding_size)}px; border: none;")
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)  
        shadow = Drop_Shadow()
        self.setGraphicsEffect(shadow)
        
        # change color based on disable
        if disabled: 
            self.setStyleSheet("margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")
            self.setEnabled(False)
        else:
            self.setStyleSheet("margin-bottom:30px; background-color:#F9FF89; border: 3px solid black; border-radius: 20%")
            self.setEnabled(True)
        self.setFixedSize(bt_w, bt_h)


        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

class BtnDone(QPushButton):
    """
    Creates the generic Button
    """
    def __init__(self, text="Done", bt_w = 140, bt_h = 101, padding_size = 20, parent=None):
        super().__init__(parent)
        self.label = QLabel(text, self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(parent.ff_inter, 20))
        self.label.setStyleSheet(f"padding: {str(padding_size)}px; border: none;")
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)  
        shadow = Drop_Shadow()
        self.setGraphicsEffect(shadow)
        self.setStyleSheet("background-color:#74FF7D; border: 3px solid black; border-radius: 10%")
        self.setFixedSize(bt_w, bt_h)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

class BtnBack(QPushButton):
    """
    Creates the generic Button
    """
    def __init__(self, text="⬅️ Return to Home", bt_w = 214, bt_h = 50, padding_size = 10, parent=None):
        super().__init__(parent)
        self.label = QLabel(text, self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(parent.ff_inter, 9))
        self.label.setStyleSheet(f"font-weight: bold; padding-top: {str(padding_size)}px; border: none;")
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)  
        # self.setStyleSheet("background-color: transparent;") # for windows, 
        self.setStyleSheet("background-color: none; border: none;") # for linux without proper displays 
        self.setFixedSize(bt_w, bt_h)
        self.label.move(0,0)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        