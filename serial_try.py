
import serial
import os
from dotenv import dotenv_values, load_dotenv
import time
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"port is: {port.device}")
    
load_dotenv()

# port_number= os.getenv("SERIAL_PORT")
# ser = serial.Serial(port_number, 9600, timeout=0)


    # Replace 'COM3' with the correct port for Windows or '/dev/ttyUSB0' for Linux/macOS
ser = serial.Serial('COM6', 9600, timeout=1)

print(f"Listening for data on port {ser.port}...")

while True:
    data = ser.readline().decode('utf-8').strip()
    if data:
        print(f"Received: {data}")

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
