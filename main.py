# from process.inserts import test_capture
import os
import sys
import time
import serial
from dotenv import dotenv_values, load_dotenv
from PyQt5.QtWidgets import QApplication

from util.state import *
from process.initialize import init_sequence 
from screens.rvm_interface import RVMInterface
from screens.config import load_config
from logging_config import setup_logging, lcd_logger
# import serial_try
from serial_try import flushSerial
# load_dotenv()
# port_number= os.getenv("SERIAL_PORT")
# ser = serial.Serial(port_number, 9600, timeout=0)

# this may be not important. 
# state_variables  = init_sequence()
# bottle_exist = state_variables["bottle_exist"]
# storage = state_variables["eco_brick_stored"]
# weight = state_variables["weight"] 
# session_end = False
# state = load_state()

logger = setup_logging()
config = load_config()

# comm = serial_try.init() #Serial communication

# flushSerial()
app = QApplication(sys.argv)
rvm_interface = RVMInterface(config)
rvm_interface.show()

# Start the application's event loop
sys.exit(app.exec_())
