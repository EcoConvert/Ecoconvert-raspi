import logging
from logging_config import setup_logging 
from process.blink import blink

setup_logging()

blink()
