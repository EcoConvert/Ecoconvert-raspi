from PyQt5.QtCore import QThreadPool
from .base_screen import BaseScreen
from .views.iv_bottle import setup_ui
from util.state import save_state_variables
from .controller.i2_camera import CameraThread
from logging_config import lcd_logger  

class InsertScreenBottle(BaseScreen):
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
        self.PET_POINTS = 10.0
        self.cont = False
        self.logger.debug("Initializing InsertScreenBottle")  # Log screen initialization
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
        Handle the click event to capture an image and infer the bottle type.
        """
        self.logger.info("Start button clicked, initiating capture and inference")  # Log button click
        self._capture_and_infer()

    def _capture_and_infer(self):
        """
        Capture image and start inference to identify the bottle type.
        """
        self.logger.debug("Starting inference process")  # Log the start of inference process
        pool = QThreadPool.globalInstance()
        inference = CameraThread()
        pool.start(inference)
        inference.signal.inference.connect(self.process_bottle)

    def process_bottle(self, inference=None):
        """
        Process the bottle after inference, check if valid, and proceed accordingly.
        
        Args:
            inference (bool, optional): Whether the inference was successful. Defaults to None.
        """
        self.logger.debug(f"Processing bottle: {inference}")  # Log inference result
        inference = False
        if inference:
            self.logger.info("Valid bottle detected")  # Log valid bottle detection
            save_state_variables("bottle_exist", inference)
            if self.parent():
                self.parent().setCurrentIndex(4)  # Go to QR Screen
                qr_screen = self.parent().widget(4)
                qr_screen.generate_qr(self.PET_POINTS)
                self.logger.info("Navigated to QR screen and generated QR code.")  # Log QR screen navigation and QR generation
            else:
                self.logger.warning("No parent QStackedWidget found.")  # Log if parent widget is not found
        else:
            error_screen = self.parent().widget(7)
            self.logger.error("Invalid bottle detected. Displaying error screen.")  # Log invalid bottle detection
            error_screen.spawn_error_page(
                error_code=1,
                error_message="non 1.5 pet bottle",
                action_message="Please retrieve the non 1.5 bottle<br>then press return to standby"
            )
            self.parent().setCurrentIndex(7)  # Set to error screen
            self.logger.info("Navigated to error screen with appropriate error message.")  # Log navigation to error screen
