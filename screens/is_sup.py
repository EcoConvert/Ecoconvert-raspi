import random
import logging  
from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_sup import setup_ui 
from util.state import save_state_variables, load_state_variables
from .controller.i3_camera import CameraThread2

# ✅ Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('rvm_logs/is_sup.log')
formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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
        self.weight = load_state_variables("weight")
        self.ser_weight = 0
        logger.info("[Init] SUP Insert Screen initialized with weight: %s", self.weight)  #Logging init
        setup_ui(self)
        self.done_clickability(False)
    
    def done_clickability(self, state = None):
        if state is None:
            return
        print("Done Clickability ", state)
        logger.debug("[done_clickability] Start button set to: %s", state)  # Logging button state
        self.start_button.setEnabled(state)

    def _on_click(self):
        if self.parent():
            logger.info("[_on_click] Starting SUP insertion process...")  #Logging click event
            self.process()
        else:
            self.logger.warning("No parent QStackedWidget found.")

    def _generate_points(self, val):  
        self.points = 0
        self.points = round(val * self.SUP_MULT, 2)
        print("Points sup " + str(self.points))
        logger.info("[_generate_points] Calculated points from weight: %.2f → %.2f", val, self.points)  #Logging point calculation
        pass 

    def _last_process(self):
        print("SUPS deposited")
        weight_diff = self.ser_weight - self.weight 
        print("Weight diff " + str(weight_diff))
        logger.info("[_last_process] SUP deposited. Weight diff: %s", weight_diff)  #Logging weight diff
        self._generate_points(weight_diff) 
        save_state_variables("weight", self.ser_weight)
        logger.debug("[_last_process] Updated saved weight to: %s", self.ser_weight)  #Logging weight save

        qr_screen = self.parent().widget(4)
        qr_screen.generate_qr(self.points)
        logger.info("[_last_process] QR generated. Transitioning to QR screen.")  #Logging QR screen transition
        self.parent().setCurrentIndex(4) # go to SUP Screen  
    
    def process(self):
        self.weight = load_state_variables("weight")
        self.ser_weight = 0
        logger.debug("[process] Reloaded weight from state: %s", self.weight)  #Logging process weight reload

        pool = QThreadPool.globalInstance()
        inference = CameraThread2()
        pool.start(inference)
        inference.signal.inference.connect(self.is_valid_plastic)
        print("processing sup")
        logger.info("[process] CameraThread2 started for SUP detection.")  #Logging thread start

    def is_valid_plastic(self, inference):
        inference = "err"  # NOTE: Static inference; expected to be dynamic in real implementation
        logger.debug("[is_valid_plastic] Inference result: %s", inference)  #Logging raw inference
        if inference == "plastic":
            self.ser_weight = self.weight + random.randint(1, 100)
            print("[is_sup.py] weight ", self.weight)
            print("[is_sup.py] ser ", self.ser_weight)
            logger.info("[is_valid_plastic] Valid SUP detected. Simulated ser_weight: %s", self.ser_weight)  #Logging simulated weight
            self._last_process()
        else:
            error_screen = self.parent().widget(7)
            error_screen.spawn_error_page(
                error_code=2,
                error_message="non sup item",
                action_message="Please retrieve the non plastic item<br>then press return to standby"
            )
            logger.warning("[is_valid_plastic] Invalid item detected. Redirecting to error screen.")  #Logging error redirect
            self.parent().setCurrentIndex(7)
