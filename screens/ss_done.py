from .base_screen import BaseScreen
from .views.sv_done import setup_ui
from logging_config import lcd_logger 

class StandbyScreenDone(BaseScreen):
    """
    BOTH SUP AND BOTTLE DISABLED. Screen for the RVM LCD Interface. 
    """

    def __init__(self, config, parent=None):
        """
        Initialize the welcome screen.
        Args:
            config (dict): Application configuration dictionary.
            parent (QStackedWidget, optional): Parent stacked widget for navigation.
        """
        super().__init__(config, parent)  # Inherit from BaseScreen
        # self._setup_ui()

        # this is the new updated way to set up UI. it is divergent from the Object oriented programming because I personally find functional programming more straightforward
        # from self._setup_ui() delete the move the self as parameter, then delete the underscore
        # then hook it up on the views.   
        setup_ui(self)

        # Logger
        self.logger = lcd_logger(__name__)  # Initialize logger for StandbyScreenDone
        self.logger.debug("StandbyScreenDone initialized.")  # Log initialization of the screen
    
    def _on_click(self):
        if self.parent():
            self.parent().setCurrentIndex(6)
            self.update_state(3)
            processing_screen = self.parent().widget(6)
            processing_screen.wait_for_serial_done()
            # process
            self.logger.info("Transitioning to Processing Screen.")  # Log the transition to the processing screen
