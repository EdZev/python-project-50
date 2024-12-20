import os
import pytest
from gendiff.parser import get_data

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def get_file_path(file_name):
    return os.path.join(FIXTURES_PATH, file_name)


def test_json_file_not_foud():
    file_path = get_file_path('file_not_found.json')
    with pytest.raises(Exception) as e:
        get_data(file_path)
    assert str(e.value) == f'File not found {file_path}'


def test_yaml_file_not_foud():
    file_path = get_file_path('file_not_found.yaml')
    with pytest.raises(Exception) as e:
        get_data(file_path)
    assert str(e.value) == f'File not found {file_path}'


def test_unsupported_file_format():
    file_path = get_file_path('file.err')
    with pytest.raises(Exception) as e:
        get_data(file_path)
    assert str(e.value) == f'Unsupported file format {file_path}'


def test_bad_json():
    with pytest.raises(Exception) as e:
        file_path = get_file_path('json_error.json')
        get_data(file_path)
    assert str(e.value) == f'Invalid JSON file {file_path}'


def test_bad_yaml():
    with pytest.raises(Exception) as e:
        file_path = get_file_path('yaml_error.yaml')
        get_data(file_path)
    assert str(e.value) == f'Invalid YAML file {file_path}'
