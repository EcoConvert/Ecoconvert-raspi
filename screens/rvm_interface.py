# src/lcd_interface/screens/rvm_interface.py
from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from util.state import * # load_state, save_state, load_state_variables, save_state_variables
from logging_config import lcd_logger
from .completion_screen import CompletionScreen
from .dummy_detection import DetectionResultScreen
from .processing_screen import ProcessingScreen
from .reminder_screen import ReminderScreen
from .welcome_screen import WelcomeScreen


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

    def _setup_screens(self):
        """
        Create and add screens to the stacked widget.
        """
        try:
            # Welcome Screen (index 0)
            welcome_screen = WelcomeScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(welcome_screen)

            # Reminder Screen (index 1)
            reminder_screen = ReminderScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(reminder_screen)

            # Processing Screen (index 2) - Pass the Camera instance
            processing_screen = ProcessingScreen(self.config, self.stacked_widget, None)
            self.stacked_widget.addWidget(processing_screen)

            # Detection Result Screen (index 3)
            detection_screen = DetectionResultScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(detection_screen)

            # Completion Screen (index 4)
            completion_screen = CompletionScreen(self.config, self.stacked_widget)
            self.stacked_widget.addWidget(completion_screen)

            # Set the initial screen
            self.stacked_widget.setCurrentIndex(0)

            self.logger.info("Screens initialized successfully.")
        except Exception as e:
            self.logger.error(f"Error setting up screens: {e}", exc_info=True)
            raise
    
    # from here on, we manage the state based on what is the index number

    def manage_state(self):
        
        self.state = load_state()

        pass 