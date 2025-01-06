# from process.inserts import test_capture
from process.initialize import init_sequence 
from util.global_state import load_global_state, save_global_state

data  = init_sequence()
bottle_exist = data["bottle_exist"]
storage = data["eco_brick_stored"]
weight = data["weight"]  
session_end = False

state_flags = [0,0,0]
 
"""
if button_pressed: 
    session_end = False
    start_session() # all the checks and whatnots
    save new params to global state 
    retriger load_global_state() beacause things will change 
    session_end = True 
"""


if bottle_exist & session_end: 
    print("Bottle exist do not accept more")
    state_flags[0] = 1
else: 
    print("provide atleast one bottle")

if weight > 529 & session_end: #529 can be changed, 529 = 23 * 23
    print("Storage is full get the plastic SUP")
    # call the function to empty the storage
    # empty_storage()
    # reset the storage
    state_flags[1] = 1

if storage > 3:  
    print("Storage is full get the finished ecobrick")
    # call the function to empty the storage
    # empty_storage()
    # reset the storage
    # call the function to empty the storage
    # empty_storage()
    # reset the storage
    state_flags[2] = 1

if state_flags == [1,1,0]:
    print("Start the machine")
    # disable start session 
    # synchronous code until finished. 
    # enable start session
    save_global_state(False, 0, storage+1)
    state_flags = [0,0,0]
    load_global_state()

if state_flags == [0,0,1]:
    print("Collect finished ecobrick")