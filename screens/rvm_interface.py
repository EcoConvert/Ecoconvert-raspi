# src/lcd_interface/screens/rvm_interface.py
from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from util.state import * # load_state, save_state, load_state_variables, save_state_variables
from logging_config import lcd_logger
from .processing_screen import ProcessingScreen
from .standby_screen import StandbyScreen
from .welcome_screen import WelcomeScreen
from .is_bottle import InsertScreenBottle
from .is_sup import InsertScreenSup
from .error_screen import ErrorScreen 
from .ss_done import StandbyScreenDone
from .qr_screen import QrScreen
from .ecobrick_screen import EcoScreen

class RVMInterface(QWidget):
    """
    Main interface for the RVM LCD application.

    Manages screen navigation and the overall application flow.
    """

    def __init__(self, config):
        """
        Initialize the RVM interface.

        Args:
            config (dict): Application configuration dictionary.
        """
        super().__init__()
        self.state = load_state()
        self.managed_index = None
        # Logger
        self.logger = lcd_logger(__name__)
        self.logger.info("RVMInterface initialized.")  # Logging
        # Configuration
        self.config = config
        # Setup main window
        self._setup_window()
        # Setup screens
        self._setup_screens()
        
    def _setup_window(self):
        """
        Configure the main application window.
        """
        self.setWindowTitle(self.config.get("window_title", "RVM LCD Interface"))
        self.setGeometry(
            100,
            100,
            self.config.get("window_width", 480),
            self.config.get("window_height", 320),
        )

        # Main layout
        layout = QVBoxLayout()

        # Create stacked widget for screen management
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)
        self.logger.info("Main window setup completed.")  # Logging

    def _setup_screens(self):
        """
        Create and add screens to the stacked widget.
        """
        try:
            # ----------------------------------------------------------------------
            # ecobrick_screen = EcoScreen(self.config, self.stacked_widget)
            # self.stacked_widget.addWidget(ecobrick_screen)
            # qr_screen = QrScreen(self.config, self.stacked_widget)
            # self.stacked_widget.addWidget(qr_screen)
            # error_screen = ErrorScreen(self.config, self.stacked_widget)
            # self.stacked_widget.addWidget(error_screen)
            #  ------------------------------------------------------------------------

            # Welcome Screen (index 0)
            welcome_screen = WelcomeScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(welcome_screen)
            self.logger.info("Welcome screen added at index 0.")  # Logging

            # Standby Screen (index 1)
            standby_screen = StandbyScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(standby_screen)
            self.logger.info("Standby screen added at index 1.")  # Logging
            # Insert Screen bottle (index 2)
            is_bottle = InsertScreenBottle(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(is_bottle)
            self.logger.info("Insert bottle screen added at index 2.")  # Logging

            # Insert Screen sup (index 3)
            is_sup = InsertScreenSup(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(is_sup)
            self.logger.info("Insert SUP screen added at index 3.") # Logging

            # QR Screen (index 4)
            qr_screen = QrScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(qr_screen)
            self.logger.info("QR screen added at index 4.")  # Logging

            # Standby Screen Done (index 5)
            ss_done = StandbyScreenDone(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(ss_done)
            self.logger.info("Standby done screen added at index 5.")  # Logging

            # Processing Screen (index 6) - Pass the Camera instance
            processing_screen = ProcessingScreen(self.config, self.stacked_widget, None)
            self.stacked_widget.addWidget(processing_screen)
            self.logger.info("Processing screen added at index 6.")  # Logging
            # Error Screen (index 7)
            error_screen = ErrorScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(error_screen)
            self.logger.info("Error screen added at index 7.")  # Logging

            # Ecobrick Retrieve Mode Result Screen (index 8)
            ecobrick_screen = EcoScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(ecobrick_screen)
            self.logger.info("Ecobrick screen added at index 8.")  # Logging

            # Set the initial screen
            self.stacked_widget.setCurrentIndex(0)
            self.logger.info("Initial screen set to index 0.")  # Logging

            self.logger.info("Screens initialized successfully.")
        except Exception as e:
            self.logger.error(f"Error setting up screens: {e}", exc_info=True)  # Logging
            raise

    # from here on, we manage the state based on what is the index number
