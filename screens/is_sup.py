import random
from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_sup import setup_ui
from util.state import save_state_variables, load_state_variables
from .controller.i3_camera import CameraThread2
from logging_config import lcd_logger  

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
        self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this screen
        self.SUP_MULT = 0.2
        self.weight = load_state_variables("weight")
        self.ser_weight = 0
        self.logger.debug("Initializing InsertScreenSup")  # Log screen initialization
        setup_ui(self)
        self.done_clickability(False)
    
    def done_clickability(self, state=None):
        """
        Control the clickability of the Done button.
        
        Args:
            state (bool, optional): Enable or disable the button. Defaults to None.
        """
        if state is None:
            return
        self.logger.debug(f"Setting Done button clickability to {state}")  # Log button state change
        print("Done Clickability ", state)
        self.start_button.setEnabled(state)

    def _on_click(self):
        """
        Handle the click event to start processing.
        """
        self.logger.info("Start button clicked, initiating process")  # Log button click
        if self.parent():
            self.process()
        else:
            self.logger.warning("No parent QStackedWidget found.")  # Log if parent widget is not found
    
    def _generate_points(self, val):
        """
        Generate points based on the given value.
        
        Args:
            val (float): Value used to calculate points.
        """
        self.points = round(val * self.SUP_MULT, 2)
        self.logger.debug(f"Generated points: {self.points}")  # Log generated points
        print("Points sup " + str(self.points))
    
    def _last_process(self):
        """
        Process the last step, including calculating weight and generating QR code.
        """
        self.logger.debug("Performing last process step")  # Log last process
        print("SUPS deposited")
        self.weight = self.weight + self.ser_weight
        self.logger.debug(f"Weight difference: {self.ser_weight}")  # Log weight difference
        print("serial weight on generate points ",  str(self.ser_weight))   
        self._generate_points(self.ser_weight)
        save_state_variables("weight", self.weight)
        qr_screen = self.parent().widget(4)
        qr_screen.generate_qr(self.points)
        self.logger.info(f"Generated QR code with {self.points} points.") # Log QR generationn
        self.parent().setCurrentIndex(4)  # Go to QR Screen
    
    def process(self):
        """
        Start the process of capturing and inferring plastic items.
        """
        self.logger.debug("Starting process to capture and infer plastic items")  # Log process start
        self.weight = load_state_variables("weight")
        self.ser_weight = 0
        
        # Start camera thread
        pool = QThreadPool.globalInstance()
        inference = CameraThread2()
        pool.start(inference)
        inference.signal.inference.connect(self.is_valid_plastic)
        self.logger.info("Camera thread started for plastic inference")  # Log camera thread start
        print("processing sup")
    
    def is_valid_plastic(self, inference):
        """
        Check if the detected item is a valid plastic and process accordingly.
        
        Args:
            inference (str): Inference result, expected to be 'plastic' for valid items.
        """
        self.logger.debug(f"Received inference result: {inference}")  # Log inference result
        
        if inference:
            # Simulating weight processing
            weight_change = round(random.uniform(0.001, 0.300), 5)
            print("value from arduino" , weight_change)
            self.ser_weight= (weight_change * 1000)
            self.weight = self.weight + self.ser_weight   # Simulating weight change
            self.logger.debug(f"Weight: {self.weight}, Processed Weight: {self.ser_weight}")  # Log weight data
            self._last_process()
        else:
            self.logger.error("Invalid item detected: non-plastic")  # Log invalid item detection
            error_screen = self.parent().widget(7)
            error_screen.spawn_error_page(
                error_code=2,
                error_message="non sup item",
                action_message="Please retrieve <br> the non plastic item<br>then press <br> return to standby"
            )
            self.parent().setCurrentIndex(7)  # Set to error screen
            self.logger.info("Navigated to error screen.")  # Log navigation to error screen