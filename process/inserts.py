import logging
import sys
import os

from modules.Camera import Camera
from modules.lcd_main import RVMInterface
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logging_config import setup_logging

setup_logging()

def test_capture():
    try:
        cam = Camera(0)
        cam.init_camera()

        labels = cam.load_labels()
        print("Labels:", labels)

        inference = cam.capture_and_infer()
        print(inference)

        if inference.lower() == "metal":
            print("Metal")

    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        cam.release_camera()

def main(): 
    app = QApplication(sys.argv)
    lcd = RVMInterface()
    lcd.show()
    sys.exit(app.exec_())   


if __name__ == "__main__":
    main() 
