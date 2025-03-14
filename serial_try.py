
import serial
import os
from dotenv import dotenv_values, load_dotenv
import time
import serial.tools.list_ports

ser = serial.Serial('COM12', 9600, timeout=1)  
time.sleep(2)  # Wait for Arduino to initialize

print("Listening for data from Arduino...")

while True:
    ser.write(b"Hello Arduino!\n")  # Send data to Arduino
    time.sleep(1)

    data = ser.readline().decode('utf-8').strip()  # Read response from Arduino
    if data:
        print(f"Received from Arduino: {data}\n")


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
