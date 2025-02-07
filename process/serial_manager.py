import os
import serial
from dotenv import load_dotenv
from util.state import save_state
class SerialManager:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SerialManager, cls).__new__(cls)
            cls._instance.init_serial()
        return cls._instance

    def init_serial(self):
        try:
            load_dotenv()
            port_number = os.getenv("SERIAL_PORT")

            if not port_number:
                raise ValueError("SERIAL_PORT not set in .env file")

            self.ser = serial.Serial(port_number, 9600, timeout=0)
            if not self.ser.is_open:
                raise IOError("Serial port failed to open")
        except IOError as e: 
            print("failed daw to open beh")
        except ValueError as e:
            print(e)

    def write(self, data):
        """Write data to the serial port"""
        try:
            self.ser.write(str(str(data)).encode()) # this double string conversion, idk why but it works. Do not remove or state 2 and 3 will not work.
            save_state(data)
            print(f"Sent: {str(data).encode()}")
        except Exception as e:
            print(f"Serial write error: {e}")

# Global instance
serial_manager = SerialManager()