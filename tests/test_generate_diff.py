import os
from gendiff.generate_diff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_path):
    with open(file_path, encoding='utf8') as f:
        return f.read()


def test_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_path = os.path.join(FIXTURES_PATH, 'diff.txt')
    expected = read_fixture(expected_path)
    result = generate_diff(file_path1, file_path2)
    assert result == expected


def test_yaml():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yaml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_path = os.path.join(FIXTURES_PATH, 'diff.txt')
    expected = read_fixture(expected_path)
    result = generate_diff(file_path1, file_path2)
    assert result == expected


def test_yaml_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yaml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_path = os.path.join(FIXTURES_PATH, 'diff.txt')
    expected = read_fixture(expected_path)
    result = generate_diff(file_path1, file_path2)
    assert result == expected
