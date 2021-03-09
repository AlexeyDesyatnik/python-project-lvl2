import argparse
import json


def format_key(name, value, state_char=' ', indent=2):
    return "{}{} {}: {}".format(
        ' ' * indent,
        state_char,
        name,
        value)


def report_dictionary_diff(dict1, dict2):
    all_keys = dict1.keys() | dict2.keys()
    removed_keys = dict1.keys() - dict2.keys()
    added_keys = dict2.keys() - dict1.keys()
    report = ['{']
    for name in sorted(all_keys):
        line2 = None
        if name in removed_keys:
            line1 = format_key(name, dict1[name], state_char='-')
        elif name in added_keys:
            line1 = format_key(name, dict2[name], state_char='+')
        else:
            if dict1[name] == dict2[name]:
                line1 = format_key(name, dict1[name], state_char=' ')
            else:
                line1 = format_key(name, dict1[name], state_char='-')
                line2 = format_key(name, dict2[name], state_char='+')
        report.append(line1)
        if line2:
            report.append(line2)
    report.append('}')
    return report


def generate_diff(fname1, fname2):
    dict1 = json.load(open(fname1))
    dict2 = json.load(open(fname2))
    report = report_dictionary_diff(dict1, dict2)
    return '\n'.join(report)


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
