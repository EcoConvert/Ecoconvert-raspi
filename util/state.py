import json

def load_state_variables():

    with open('state_variables.json', 'r') as f:
        data = json.load(f)
        return data

def save_state_variables(bottle, storage, weight):
    """
    save in order of if bottle exist, # of ecobrick in storage, weight of SUP in grams
    """
 
    data = {"weight": weight, "storage": storage, "bottle": bottle}
    with open('state_variables.json', 'w') as f:
        json.dump(data, f)

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