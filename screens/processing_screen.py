from functools import partial
from PyQt5.QtCore import  QThreadPool, QObject, QTimer

from PyQt5.QtWidgets import QApplication
from .base_screen import BaseScreen
from .views.processing_view import setup_ui
from util.state import save_state_variables, load_state_variables
from screens.controller.i4_ecob_process import SerialWorker
# from serial_try import readEcoBrickWeight, ser

class ProcessingScreen(BaseScreen):
    """
    Simulated Processing Screen for the RVM LCD Interface.
    """

    def __init__(self, config, parent=None, camera=None):
        super().__init__(config, parent, camera)
        
        self.progress_value = 0  # Current progress value

        self.isDone = 0
        self.thread_pool = QThreadPool()
        self.worker = SerialWorker()
        self.timer = QTimer()
        self.logger.debug("Initializing Processing Screen")  # Log screen initialization

        setup_ui(self)
    
    
    # First function being called
    def wait_for_serial_done(self):
        """
        Wait for the done signal.
        """
        self.logger.info("Waiting for serial done signal") 
        self._serial_read()    
    
    def _on_serial_done(self):
        self.progress_bar.setValue(100)
        # Store previous value
        bricks = load_state_variables("eco_brick_stored")
        # Increment the number of bricks
        save_state_variables("eco_brick_stored", bricks + 1)
        
        # Reset values
        self.isDone = False
        save_state_variables("weight", 0.0)
        save_state_variables("bottle_exist", False)
        self.logger.info("Serial done")  # Log serial done event

        standby_screen = self.parent().widget(1)
        standby_screen.pet_clickability(True)
        standby_screen.sup_clickability(True)
        self.timer.singleShot(1000, self._ready_to_go_back)

    def _ready_to_go_back(self):
        self.progress_bar.setValue(0)
        self.parent().setCurrentIndex(1) # Standby Screen
        self.update_state(0)
        self.logger.info("Ready to go back to standby screen: Progress bar reset")  # Log ready to standby screen 

    def _serial_read (self):
        """
        Simulate serial reads. in the future make this a QRunabble for threading 
        """
        self.worker.signal.data_received.connect(self._read_and_write)
        self.thread_pool.start(self.worker)
        
    def _read_and_write(self, data):
        """
            We can send a 'done' signal only when the ecobrick is stored
            instead of constantly reading the weight.
            This is to avoid overloading the serial port with data.
        """
        self.isDone = data
        if (self.isDone == 'H'):
            self.worker.stop()
            self._on_serial_done()
        else:
            print(f"Invalid data received: {data}")