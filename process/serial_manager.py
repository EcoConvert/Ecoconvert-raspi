import os
import serial
import time
from dotenv import load_dotenv
from util.state import save_state

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

            self.ser = serial.Serial(port_number, 115200, timeout=0)
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
        try:
            if self.ser and self.ser.is_open:
                data = self.ser.readline().decode("utf-8").strip()
                if type(float(data)) == float:
                    return float(data), 
        except Exception as e:
            print(f"Serial write error: {e}")
    
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
            self.ser.write(str(str(data)).encode())
            print(f"Sent: {str(data).encode()}")
        except Exception as e:
            print(f"Serial write error: {e}")
        save_state(data)
        

# Global instance
serial_manager = SerialManager()

