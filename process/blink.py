# replace the main.py on the top level directory with this code. to run blinkers along with a similar coded ardunio code.
import os
import time
import serial

from process.initialize import init_sequence 
from util.state import *
from dotenv import dotenv_values, load_dotenv

load_dotenv()

port_number= os.getenv("SERIAL_PORT")
ser = serial.Serial(port_number, 9600, timeout=0)

# state variables here. They say how the RVM is doing.
state_variables  = init_sequence()
bottle_exist = state_variables["bottle_exist"]
storage = state_variables["eco_brick_stored"]
weight = state_variables["weight"]  
state = load_state()
session_end = False

state_flags = [0,0,0] # I will change this state flag array here, It seems to lost its purpose because of state.json. 
 
"""
if button_pressed: 
    session_end = False
    start_session() # all the checks and whatnots
        bottle_exist = True
        weight += DEPOSITED_WEIGHT
    save new params to global state 
    retriger load_global_state() beacause things will change 
    make QR 
    session_end = True 
"""
# do some initializing here 
while True: 
    if state == 0: # Standby Mode
        # Show Welcome Screen    
        # make the serial state writing only happen once. 
        ser.write(b'0') # serial write to arduino to change the state 
        # functionalize anything that follows on process folder
        
    elif state == 1:# Insert Mode
        # make the serial state writing only happen once. 
        ser.write(b'1')
        # functionalize anything that follows on process folder
        if bottle_exist: 
            print("Bottle exist do not accept more")

        if weight > 529:  #529 can be changed, 529 = 23 * 23
            print("Storage is full get the plastic SUP")

    elif state == 2: # Processing Mode 
        # make the serial state writing only happen once. 
        ser.write(b'2')
        # functionalize anything that follows on process folder
        if bottle_exist & weight > 529: 
            print("Bottle exist and SUP is full")         
        
    elif state == 3: # Retrieve Mode
        # make the serial state writing only happen once. 
        ser.write(b'3')
        # functionalize anything that follows on process folder
        if storage > 3:  
            print("Storage is full get the finished ecobrick")
