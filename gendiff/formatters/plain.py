def get_prepared_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def build_str(line):
    path = '.'.join(line['parents'])
    if line['status'] == 'added':
        value = get_prepared_value(line['value'])
        return f"Property '{path}' was added with value: {value}"

    if line['status'] == 'removed':
        value = get_prepared_value(line['value'])
        return f"Property '{path}' was removed"

    old_value = get_prepared_value(line['old_value'])
    new_value = get_prepared_value(line['new_value'])
    return f"Property '{path}' was updated. From {old_value} to {new_value}"


def get_modified_lines(key, value, parents):
    if not isinstance(value, dict) and 'status' not in value:
        return
    if value['status'] == 'changed':
        return {
            'status': value['status'],
            'old_value': value['old_value'],
            'new_value': value['new_value'],
            'parents': [*parents, key],
        }
    if not value['status'] == 'unchanged':
        return {
            'status': value['status'],
            'value': value['value'],
            'parents': [*parents, key],
        }
    return build_line(value['value'], [*parents, key])


def build_line(diff, parents=[]):
    if not isinstance(diff, dict):
        return
    lines = []
    for key, value in diff.items():
        line = get_modified_lines(key, value, parents)
        if line and isinstance(line, list):
            lines = [*lines, *line]
        elif line:
            lines.append(line)
    return lines


def plain(diff):
    changed_lines = build_line(diff)
    lines = map(build_str, changed_lines)
    # print(f'diff - {list(lines)}')
    return '\n'.join(list(lines))
