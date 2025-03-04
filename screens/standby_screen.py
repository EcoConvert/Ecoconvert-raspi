# src/lcd_interface/screens/reminder_screen.py
import time
from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject

from .base_screen import BaseScreen
from .views.standby_view import setup_ui
from .controller.i0_init import InitThread

class StandbyScreen(BaseScreen):
    """
    Standby Screen with all the logic you might need. 
    """

    def __init__(self, config, parent=None):
        super().__init__(config, parent)
        setup_ui(self)

    def _on_click_pet(self):
        if self.parent():
            self.parent().setCurrentIndex(2) # go to PET Screen  
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")

    def _on_click_sup(self):
        if self.parent():
            self.parent().setCurrentIndex(3) # go to SUP Screen  
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")
    
    def sup_clickability(self, state = True):

        self.sup_button.setEnabled(state)
    
    # ###### 
    def global_state_checker(self):
        pool = QThreadPool.globalInstance()
        worker = InitThread()
        pool.start(worker)

        # Connect signal dynamically
        worker.signal.show.connect(self._change_screen)
        


    def _change_screen(self, screen_index):
        if self.parent():
            self.parent().setCurrentIndex(screen_index)
