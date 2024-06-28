import sys
import clipboard
import json


SAVED_DATA = r"code_projects\clip_board.json"


def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key= input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data  copied to clipboard.")
        else:
            print("Key does not exist.")

    elif command == "list":
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("unknown command")
else:
    print("one command only")
