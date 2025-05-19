import os
import serial
import serial.tools.list_ports
import time
from dotenv import load_dotenv
from util.state import save_state
from serial_try import writeCommand

class SerialManager:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SerialManager, cls).__new__(cls)
            cls._instance.init_serial()
            # cls._instance.ser = None
        return cls._instance

    def init_serial(self):
        print(serial)
        print
        try:
            load_dotenv()
            port_number = os.getenv("SERIAL_PORT")
            if not port_number:
                raise ValueError("SERIAL_PORT not set in .env file")

            self.ser = serial.Serial(port_number, 9600, timeout=1)
            time.sleep(2)  # Wait for Arduino to initialize
            print("Listening for data from Arduino...")

            if not self.ser.is_open:
                raise IOError("Serial port failed to open")
        except Exception as e:
            self.ser = None
            print(f"An error occurred: {e}")

    def writeCommand(self, data):
        """Write data to the serial port"""
        command = data + '\n'
        if self.ser.open:
            self.ser.write(command.encode("utf-8"))
            self.ser.flush()
            print(f"\nSent to Arduino: {data}\n")
        else:
            print("Serial port is not open")
        
    def flushSerial(self):
        """Clearing the serial buffer"""
        if self.ser.open:
            self.ser.flushInput()
            self.ser.flushOutput()
            print("Serial buffer flushed")
        else: 
            print("Serial port is not open")
            
    def readSUPWeight(self):
        if self.ser and self.ser.is_open:
            data = self.ser.readline().decode("utf-8").strip()
            if data:
                if data.isdigit():
                    print(f"Received from Arduino: {data}\n")
                    return int(data)
            else:
                print("Invalid SUP weight data from Arduino")
                # return None
                return 0 # return 0 instead
        else:
            print("Serial port is not open")
            return 0
    
    def readEcoBrickWeight(self):
        data = self.ser.readline().decode("utf-8").strip()
        if data:
            if data.isdigit():
                print(f"Received from Arduino: {data}\n")
                return int(data)
            if data.isalpha():
                print(f"Received from Arduino: {data}\n")
                return data
        else:
            print("Invalid EcoBrick weight data from Arduino")
            return None
    
    def write(self, data):
        """Write data to the serial port"""
        try:
            self.ser.write(str(str(data)).encode()) # this double string conversion, idk why but it works. Do not remove or state 2 and 3 will not work.
            print(f"Sent: {str(data).encode()}")
        except Exception as e:
            print(f"Serial write error: {e}")
        save_state(data)
        

# Global instance
serial_manager = SerialManager()

