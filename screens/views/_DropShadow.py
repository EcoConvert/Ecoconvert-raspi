from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from logging_config import lcd_logger 

class Drop_Shadow(QGraphicsDropShadowEffect):
    """
    This creates the generic drop shadow that is used in the program. onteng design lang para masabing may effort pa din
    """
    def __init__(self, offset_x=0, offset_y=7, blur_radius=7, color="#25000000", parent=None):
        super().__init__(parent)
        
        # Initialize logger for this class/module with class name
        self.logger = lcd_logger(self.__class__.__name__)
        self.logger.debug("Initializing Drop_Shadow effect")  # Logging added
        
        self.setOffset(offset_x, offset_y)   # Shadow offset (x, y)
        self.logger.debug(f"Shadow offset set to: ({offset_x}, {offset_y})")  # Logging added
        
        self.setBlurRadius(blur_radius)      # Blur radius
        self.logger.debug(f"Shadow blur radius set to: {blur_radius}")  # Logging added
        
        self.setColor(QColor(color))         # Shadow color (25% black)
        self.logger.debug(f"Shadow color set to: {color}")  # Logging added
