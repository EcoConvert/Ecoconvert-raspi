
import serial
import os
from dotenv import dotenv_values, load_dotenv
import time

ser = serial.Serial(os.getenv("SERIAL_PORT"), 115200, timeout=5)  

time.sleep(2)  # Wait for Arduino to initialize

print("Listening for data from Arduino...")


def write(command):
    # ser.write(str(str(command)).encode())
    # data = ser.read_until(b'\n').decode("utf-8").strip()
    ser.write(command.encode())
    data = ser.readline().decode("utf-8").strip()
    print(data)
    
# command = "0" 
# write(command); 

inc = 8; 
while (True):   
    inc = input("press 9 to quit others to do something: ")
    if (inc =="9"):
        break
    write(inc)

