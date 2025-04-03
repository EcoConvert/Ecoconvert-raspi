import os
import serial
import serial.tools.list_ports
import time
from dotenv import load_dotenv
from util.state import save_state


class SerialManager:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SerialManager, cls).__new__(cls)
            cls._instance.init_serial()
            cls._instance.ser = None
        return cls._instance

    def init_serial(self):
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
        except IOError as e: 
            print("failed daw to open beh")
        except ValueError as e:
            print(e)
        except Exception as e:
            self.ser = None
            print(f"An error occurred: {e}")

    def writeCommand(self, data):
        """Write data to the serial port"""
        command = data + '\n'
        if self.ser and self.ser.is_open:
            self.ser.write(command.encode("utf-8"))
            self.ser.flush()
            print(f"\nSent to Arduino: {data}\n")
        else:
            print("Serial port is not open")
        
    def flushSerial(self):
        """Clearing the serial buffer"""
        if self.ser.isOpen():
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

        

# Global instance
serial_manager = SerialManager()


"""

import serial
import os
from dotenv import dotenv_values, load_dotenv
import time
import serial.tools.list_ports

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)  
# ser = serial.Serial('COM3', 9600, timeout=1)  
time.sleep(2)  # Wait for Arduino to initialize

print("Listening for data from Arduino...")

# For debug only, (int) weight of Ecobrick is the real world data
# def readBool():
#     data = ser.readline().decode("utf-8").strip()
#     if data:
#         print(f"Received from Arduino: {data}\n")
#         if data == 1:
#             return True
#         elif data == 0:
#             return False
#         else:
#             print("Invalid bool data from Arduino")
#             return None

def flushSerial(self):
    if self.ser.isOpen():
        self.ser.flushInput()
        self.ser.flushOutput()
        print("Serial buffer flushed")
    else: 
        print("Serial port is not open")
        

def writeCommand(data):
    command = data + '\n'
    if ser.open:
        ser.write(command.encode("utf-8"))
        ser.flush()
        print(f"\nSent to Arduino: {data}\n")
    else:
        print("Serial port is not open")
        
def readSUPWeight():
    data = ser.readline().decode("utf-8").strip()
    if data:
        if data.isdigit():
            print(f"Received from Arduino: {data}\n")
            return int(data)
    else:
        print("Invalid SUP weight data from Arduino")
        # return None
        return 0 # return 0 instead
    
def readEcoBrickWeight():
    data = ser.readline().decode("utf-8").strip()
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
    
    
# while True:
#     ser.write(b"Hello Arduino!\n")  # Send data to Arduino
#     time.sleep(1)

#     data = ser.readline().decode('utf-8').strip()  # Read response from Arduino
#     if data:
#         print(f"Received from Arduino: {data}\n")


# def read():
#     res = ser.readline(100).decode("utf-8")
#     print(res)

# def write():
#     isSerialInit = True
#     while True:
#         if (isSerialInit):
#             # nah bro this is unecessary, it needs handshake rather than a 2 second delay. But this is what I can only implment, might change this later 
#             time.sleep(2)    
#             isSerialInit = False 
#         ser.write(b'0')
#         read()
#         time.sleep(.2)
#         ser.write(b'1')
#         read()
#         time.sleep(.2)
#         ser.write(b'2')
#         read()
#         time.sleep(.2)
#         ser.write(b'3')
#         read()
#         time.sleep(.2)
# write()

"""