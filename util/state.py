import json

def load_state_variables(params=None):
    with open('state_variables.json', 'r') as f:
        data = json.load(f)
        return data[params] if params else data
       

def save_state_variables(key, value):
    """
    save with this layout of key value 
    {
    "weight": 0.0,
    "eco_brick_stored": 0,
    "bottle_exist": true
    }
    """
    with open('state_variables.json', 'r+') as f:
        data = json.load(f)
        # Update only key2
        data[key] = value  
        
        # Move cursor to the beginning and truncate the file before writing
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def load_state():
    with open('state.json', 'r') as f:
        data = json.load(f)
        return data["state"]

def save_state(state):
    """ State should be numerical, I am thinking of changing it to string, but for now it is numerical"""
    data = {"state": state}
    with open('state.json', 'w') as f:
        json.dump(data, f)
    
   
def main ():
    pass

if __name__ == "__main__":
    main()