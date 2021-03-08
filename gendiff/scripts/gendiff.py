import argparse
import json


def format_key(name, value, state_char=' ', indent=2):
    return "{}{} {}: {}".format(
        ' ' * indent,
        state_char,
        name,
        value)


def generate_diff(fname1, fname2):
    data1 = json.load(open(fname1))
    data2 = json.load(open(fname2))
    all_keys = data1.keys() | data2.keys()
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    output = ['{']
    for name in sorted(all_keys):
        if name in removed_keys:
            output.append(format_key(name, data1[name], state_char='-'))
        elif name in added_keys:
            output.append(format_key(name, data2[name], state_char='+'))
        else:
            if data1[name] == data2[name]:
                output.append(format_key(name, data1[name], state_char=' '))
            else:
                output.append(format_key(name, data1[name], state_char='-'))
                output.append(format_key(name, data2[name], state_char='+'))
    output.append('}')
    return '\n'.join(output)


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
