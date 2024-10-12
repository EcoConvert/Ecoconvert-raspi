import logging
from logging_config import setup_logging 
from process import inserts
# from process.blink import blink

def main():
    setup_logging()
    inserts.test_capture()
# blink()

if __name__ == "main":
    main()

