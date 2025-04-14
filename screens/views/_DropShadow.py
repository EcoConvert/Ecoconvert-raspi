from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import logging

# Initialize a module-level logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Drop_Shadow(QGraphicsDropShadowEffect):
    """
    This creates the generic drop shadow that is used in the program. onteng design lang para masabing may effort pa din
    """
    def __init__(self, offset_x=0, offset_y=7, blur_radius=7, color="#25000000", parent=None):
        logger.debug("Initializing Drop_Shadow")  #Log added
        super().__init__(parent)
        self.setOffset(offset_x, offset_y)   # Shadow offset (x, y)
        self.setBlurRadius(blur_radius)      # Blur radius
        self.setColor(QColor(color))         # Shadow color (25% black)
        logger.debug("Drop_Shadow initialized successfully")  #Log added
