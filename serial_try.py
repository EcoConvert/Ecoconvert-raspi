import serial
import os
from dotenv import dotenv_values, load_dotenv
import time

load_dotenv()

port_number= os.getenv("SERIAL_PORT")
ser = serial.Serial(port_number, 9600, timeout=0)

def read():
    res = ser.readline(100).decode("utf-8")
    print(res)

def write():
    isSerialInit = True
    while True:
        if (isSerialInit):
            # nah bro this is unecessary, it needs handshake rather than a 2 second delay. But this is what I can only implment, might change this later 
            time.sleep(2)    
            isSerialInit = False 
        ser.write(b'0')
        read()
        time.sleep(.2)
        ser.write(b'1')
        read()
        time.sleep(.2)
        ser.write(b'2')
        read()
        time.sleep(.2)
        ser.write(b'3')
        read()
        time.sleep(.2)
write()
