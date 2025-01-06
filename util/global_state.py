import json

def load_global_state():

    with open('global_state.json', 'r') as f:
        data = json.load(f)
        return data

def save_global_state(bottle, storage, weight):
    """
    save in order of if bottle exist, # of ecobrick in storage, weight of SUP in grams
    """
 
    data = {"weight": weight, "storage": storage, "bottle": bottle}
    with open('global_state.json', 'w') as f:
        json.dump(data, f)

def main ():
    pass

if __name__ == "__main__":
    main()