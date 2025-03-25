# src/lcd_interface/screens/welcome_screen.py
import random
from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_sup import setup_ui 
from util.state import save_state_variables, load_state_variables
from .controller.i3_camera import CameraThread2

class InsertScreenSup(BaseScreen):
    """
    Welcome screen for the RVM LCD Interface.
    Displays a welcome message and initial instructions.
    """

    def __init__(self, config, parent=None):
        """
        Initialize the welcome screen.
        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.SUP_MULT = 0.2
        self.weight=load_state_variables("weight")
        self.ser_weight = 0
        setup_ui(self)
        self.done_clickability(False)
    
    def done_clickability(self, state = None):
        if state is None:
            return
        print("Done Clickability ", state)
        self.start_button.setEnabled(state)

    def _on_click(self):
        if self.parent():
            self.process()
            # self.update_state(1) # update to insert 
            # qr_screen = self.parent().widget(4)
            # qr_screen.generate_qr(self.points)
            # self.parent().setCurrentIndex(4) # go to SUP Screen  
        else:
            self.logger.warning("No parent QStackedWidget found.")
    
    def _generate_points(self, val):  
        self.points = 0
        self.points = round(val * self.SUP_MULT, 2)
        print("Points sup " + str(self.points))
        pass 


    def _last_process(self):
        # open the camera here
        # some process here to get the weight 
        print("SUPS deposited")
        weight_diff = self.ser_weight - self.weight 
        print("Weight diff " + str(weight_diff))
        self._generate_points(weight_diff) 
        save_state_variables("weight", self.ser_weight)

        qr_screen = self.parent().widget(4)
        qr_screen.generate_qr(self.points)
        self.parent().setCurrentIndex(4) # go to SUP Screen  
    
    def process(self):
        # serial 
        self.weight=load_state_variables("weight")
        self.ser_weight = 0
        
        # camera thread  
        pool = QThreadPool.globalInstance()
        inference = CameraThread2()
        pool.start(inference)
        inference.signal.inference.connect(self.is_valid_plastic)
        print("processing sup")
    
    def is_valid_plastic(self, inference):
        print("inference ", inference)
        inference = "plastic" # change this latuurrs
        if inference == "plastic": # change this  kung mag class id tayo dito  
            # some process here to get the weight 
            self.ser_weight = self.weight + random.randint(1, 100) # simulation lang to ng wieght yung ginagawa ni pons mas accurate yon sa actual. 
            print("[is_sup.py] weight ", self.weight)
            print("[is_sup.py] ser ", self.ser_weight)
            self._last_process()
        else:
            print("[is_sup.py] go to error screen")
