from pathlib import Path
import json
import yaml


def parse_json(file_path):
    try:
        return json.load(open(file_path))
    except json.JSONDecodeError:
        raise ValueError(f'Invalid JSON file {file_path}')
    except FileNotFoundError:
        raise ValueError(f'File not found {file_path}')


def parse_yaml(file_path):
    try:
        return yaml.safe_load(open(file_path))
    except yaml.YAMLError:
        raise ValueError(f'Invalid YAML file {file_path}')
    except FileNotFoundError:
        raise ValueError(f'File not found {file_path}')


def get_parser(file_path):
    formats = {
        '.json': parse_json,
        '.yaml': parse_yaml,
        '.yml': parse_yaml,
    }
    try:
        return formats[Path(file_path).suffix]
    except KeyError:
        raise ValueError(f'Unsupported file format {file_path}')


def get_data(file_path):
    return get_parser(file_path)(file_path)
