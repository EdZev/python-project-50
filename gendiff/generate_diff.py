from gendiff.parser import get_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_formatter import json_formatter


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_formatter
}


def get_diff(data1, data2):
    keys = sorted(list({**data1, **data2}.keys()))
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = {
                'status': 'added',
                'value': data2[key],
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'value': data1[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'unchanged',
                'value': get_diff(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            diff[key] = {
                'status': 'unchanged',
                'value': data2[key]
            }
        else:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return diff


def generate_diff(first_file, second_file, format_name='stylish'):
    data1 = get_data(first_file)
    data2 = get_data(second_file)
    diff = get_diff(data1, data2)
    return FORMATTERS[format_name](diff)
