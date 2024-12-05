from pathlib import Path
import json
import yaml


def parse_json(file_path):
    return json.load(open(file_path))


def parse_yaml(file_path):
    return yaml.safe_load(open(file_path))


def get_data(file_path):
    formats = {
        '.json': parse_json,
        '.yaml': parse_yaml,
        '.yml': parse_yaml,
    }
    return formats[Path(file_path).suffix](file_path)
