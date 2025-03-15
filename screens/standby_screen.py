# src/lcd_interface/screens/reminder_screen.py
import time
from PyQt5.QtCore import QThreadPool
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
        self.petflag = False
        self.supflag = False
    
    def _on_click_pet(self):
        if self.parent():
            self.update_state(1)
            parent = self.parent()  
            parent.setCurrentIndex(2) # go to PET Screen
            is_bottle = parent.widget(2)
            is_bottle.process()
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")

    def _on_click_sup(self):
        if self.parent():
            self.update_state(1)
            self.parent().setCurrentIndex(3) # go to SUP Screen  
            is_sup = self.parent().widget(3)
            # self.update_state(1) # update to insert
        else:
            self.logger.warning("No parent QStackedWidget found.")
    
    def sup_clickability(self, state = True):
        self.supflag = not state 
        self.sup_btn.setEnabled(state)
        if state:
            self.sup_btn.setStyleSheet("margin-bottom:30px; background-color:#F9FF89; border: 3px solid black; border-radius: 20%")
        else:
            self.sup_btn.setStyleSheet("margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")

    def pet_clickability(self, state = True):
        self.petflag = not state 
        self.pet_btn.setEnabled(state)
        self.pet_btn.setStyleSheet("margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")
        if state:
            self.pet_btn.setStyleSheet("margin-bottom:30px; background-color:#F9FF89; border: 3px solid black; border-radius: 20%")
        else:
            self.pet_btn.setStyleSheet("margin-bottom:30px; background-color:#D9D9D9; border: 3px solid #50000000; border-radius: 20%")

    # ###### 
    def global_state_checker(self):
        pool = QThreadPool.globalInstance()
        init_worker = InitThread()
        pool.start(init_worker)

        # Connect signal dynamically
        init_worker.signal.show.connect(self._change_screen)
        init_worker.signal.pet.connect(self._change_screen)
        init_worker.signal.sup.connect(self._change_screen)

    def _change_screen(self, screen_index=None, pet=None, sup=None):
        if screen_index is not None:
            if self.parent():
                self.parent().setCurrentIndex(screen_index)

        if pet == True:
            print(f"pet triggered {pet}")
            curIndex = self.parent().currentIndex()
            if curIndex == 1:
                self.pet_clickability(False)

        if (isinstance(sup, (int, float))) and (sup >= 525.00):
            print(f"SUP action triggered: {sup}")
            curIndex = self.parent().currentIndex()
            print(f"Switched to index {curIndex}")
            if curIndex == 1:
                self.sup_clickability(False)

        if self.petflag and self.supflag:
            print("Both PET and SUP are being hit")
            parent = self.parent()  
            parent.setCurrentIndex(5) # go to PET Screen