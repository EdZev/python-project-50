def get_indent(depth):
    return ' ' * (4 * depth)


def get_prefix(status='unchanged'):
    statuses = {
        'added': '+ ',
        'removed': '- ',
        'changed': ['- ', '+ '],
        'unchanged': '  ',
    }
    return statuses[status]


def prepared_value(value, depth):
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
    prefix = get_prefix(status)

    if status == 'changed':
        old_value = prepared_value(value['old_value'], depth)
        new_value = prepared_value(value['new_value'], depth)
        deleted_line = build_str(indent, prefix[0], key, old_value)
        added_line = build_str(indent, prefix[1], key, new_value)
        return f'{deleted_line}\n{added_line}'

    value = prepared_value(value['value'], depth)
    return build_str(indent, prefix, key, value)


def build_line(key, value, depth):
    if isinstance(value, dict) and 'status' in value:
        return build_line_with_status(key, value, depth)

    return build_str(
        get_indent(depth),
        get_prefix(),
        key,
        prepared_value(value, depth)
    )


def stylish(data, depth=0):
    lines = []
    for key, value in data.items():
        lines.append(build_line(key, value, depth))
    return '{\n' + '\n'.join(lines) + f'\n{get_indent(depth)}' + '}'
