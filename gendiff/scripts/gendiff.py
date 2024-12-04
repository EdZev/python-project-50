import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    # format = args.format
    first_path = args.first_file
    second_path = args.second_file
    return generate_diff(first_path, second_path)


if __name__ == '__main__':
    main()
