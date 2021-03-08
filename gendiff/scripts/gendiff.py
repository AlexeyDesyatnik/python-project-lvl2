import argparse
import json


def generate_diff(fname1, fname2):
    data1 = json.load(open(fname1))
    data2 = json.load(open(fname2))
    print(data1)
    print(data2)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
