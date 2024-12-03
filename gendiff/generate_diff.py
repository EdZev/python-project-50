import json


def parse_json(first_file, second_file):
    first_file_data = json.load(open(first_file))
    print(first_file_data)
    second_file_data = json.load(open(second_file))
    print(second_file_data)
