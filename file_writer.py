import json


def write_to_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, ensure_ascii=False)
