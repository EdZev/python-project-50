def get_indent(depth):
    return ' ' * (4 * depth)


def get_prefix(status='not changed'):
    statuses = {
        'added': '+ ',
        'removed': '- ',
        'changed': ['- ', '+ '],
        'not changed': '  ',
    }
    return statuses[status]


def get_data(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return stylish(value, depth + 1)
    return value


def build_str(indent, prefix, key, value):
    return f'{indent}  {prefix}{key}: {value}'


def build_line_with_status(key, value, depth):
    indent = get_indent(depth)
    status = value['status']
    data = get_data(value['data'], depth)
    prefix = get_prefix(status)

    if status == 'changed':
        old_data = get_data(value['old_data'], depth)
        deleted_line = build_str(indent, prefix[0], key, old_data)
        added_line = build_str(indent, prefix[1], key, data)
        return f'{deleted_line}\n{added_line}'

    return build_str(indent, prefix, key, data)


def build_line(key, value, depth):
    if isinstance(value, dict) and 'status' in value:
        return build_line_with_status(key, value, depth)

    return build_str(
        get_indent(depth),
        get_prefix(),
        key,
        get_data(value, depth)
    )


def stylish(data, depth=0):
    lines = []
    for key, value in data.items():
        lines.append(build_line(key, value, depth))
    return '{\n' + '\n'.join(lines) + f'\n{get_indent(depth)}' + '}'
