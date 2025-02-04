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
    while True:
        ser.write(b'1')
        read()
        time.sleep(1)
        ser.write(b'0')
        read()
        time.sleep(1)
write()
