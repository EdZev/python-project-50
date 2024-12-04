import json


def get_data(path):
    return json.load(open(path))


def get_line(prefix, key, data):
    return f'  {prefix} {key}: {data}'


def generate_diff(first_file, second_file):
    data1 = get_data(first_file)
    data2 = get_data(second_file)
    keys = list({**data1, **data2}.keys())
    keys.sort()
    diff = []
    for key in keys:
        if key not in data1:
            diff.append(get_line('+', key, data2[key]))
        elif key not in data2:
            diff.append(get_line('-', key, data1[key]))
        elif data1[key] == data2[key]:
            diff.append(get_line(' ', key, data2[key]))
        else:
            diff.append(get_line('-', key, data1[key]))
            diff.append(get_line('+', key, data2[key]))
    diff_str = '\n'.join(diff)
    return '{\n' + f'{diff_str}' + '\n}'
