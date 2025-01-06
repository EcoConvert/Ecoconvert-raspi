# as annoying as it is, please run it as a module from main.py in the root directory
import json
from ..util.global_state import load_global_state

def machine_reset():
    print ("Machine reset")
    pass

def init_sequence():
    machine_reset()
    data = load_global_state()
    return data

def main(): 
    init_sequence()
    

if __name__ == "__main__":
    main()