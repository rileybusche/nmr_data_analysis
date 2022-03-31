# Riley Busche 2022
import json

def write_to_file(file_path:str, data_object:dict):
    with open(file_path, 'w') as output_file:
        json.dump(data_object, output_file, indent=4)