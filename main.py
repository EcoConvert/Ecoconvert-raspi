import logging 
from logging_config import setup_logging 
#from process import inserts
from process.inserts import test_capture
# from process.blink import blink

setup_logging()
test_capture()
# blink()


