from gendiff.parser import get_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
}


def get_diff(data1, data2):
    keys = sorted(list({**data1, **data2}.keys()))
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = {
                'status': 'added',
                'data': data2[key],
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'data': data1[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'not changed',
                'data': get_diff(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            diff[key] = {
                'status': 'not changed',
                'data': data2[key]
            }
        else:
            diff[key] = {
                'status': 'changed',
                'data': data2[key],
                'old_data': data1[key]
            }
    return diff


def generate_diff(first_file, second_file, format_name='stylish'):
    data1 = get_data(first_file)
    data2 = get_data(second_file)
    diff = get_diff(data1, data2)
    return FORMATTERS[format_name](diff)
