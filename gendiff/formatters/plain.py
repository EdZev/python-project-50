def get_prepared_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def build_str(line):
    parents = '.'.join(line['parents'])
    value = get_prepared_value(line['value'])

    if line['status'] == 'added':
        return f"Property '{parents}' was added with value: {value}"

    if line['status'] == 'removed':
        return f"Property '{parents}' was removed"

    old_value = get_prepared_value(line['old_value'])
    return f"Property '{parents}' was updated. From {old_value} to {value}"


def get_modified_lines(key, value, parents):
    if not isinstance(value, dict) and 'status' not in value:
        return
    if not value['status'] == 'not changed':
        old_value = value['old_data'] if 'old_data' in value else ''
        return {
            'status': value['status'],
            'value': value['data'],
            'old_value': old_value,
            'parents': [*parents, key],
        }
    return build_line(value['data'], [*parents, key])


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
