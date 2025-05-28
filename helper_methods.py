import json

# load data from JSON file
def load_data() ->json:
    try:
        with open("data\patients.json", 'r') as f:
            data = json.load(f)
        return data
    
    except Exception as ex:
        print(f"Exception occurred while loading patients data from JSON File: {ex}")


# save data to json file
def save_data(data):
    try:
        with open("data\patients.json", 'w') as f:
            json.dump(data, f)

    except Exception as ex:
        print(f"Exception occurred while saving data in json file: {ex}") 