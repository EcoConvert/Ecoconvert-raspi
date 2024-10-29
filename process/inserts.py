import logging
import sys

from modules.Camera import Camera
from modules.lcd_main import RVMInterface
from PyQt5.QtWidgets import QApplication

def test_capture():
    try:
        cam = Camera(2)
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
    # lcd.welcome_screen()
    # lcd.processing_screen()
    # lcd.detection_screen()
    # lcd.rewards_screen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 
