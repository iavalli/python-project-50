import argparse
import json


def compare_files(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    diff = {}
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = keys1.union(keys2)

    for key in sorted(all_keys):
        if key in keys1 and key not in keys2:
            diff['- ' + key] = data1[key]
        elif key not in keys1 and key in keys2:
            diff['+ ' + key] = data2[key]
        elif data1[key] != data2[key]:
            diff['- ' + key] = data1[key]
            diff['+ ' + key] = data2[key]

    return diff


def generate_diff(file_path1, file_path2):
    diff = compare_files(file_path1, file_path2)
    
    diff_lines = [f"{key}: {value}" for key, value in diff.items()]
    return '{\n  ' + '\n  '.join(diff_lines) + '\n}'


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str, help="First configuration file")
    parser.add_argument("second_file", type=str, help="Second configuration file")
    parser.add_argument("-f", "--format", help="set format of output", choices=["plain", "json"])
    args = parser.parse_args()

    if args.format:
        # Обработка выбора формата вывода
        if args.format == "plain":
            plain_diff = generate_diff(args.first_file, args.second_file)
            print(plain_diff)
        elif args.format == "json":
            json_diff = generate_diff(args.first_file, args.second_file)
            print(json_diff)
    else:
        # Вывод разницы между файлами
        diff = generate_diff(args.first_file, args.second_file)
        print(diff)


if __name__ == '__main__':
    main()

"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file", type=str, help = "")
    parser.add_argument("second_file", type=str, help = "")
    parser.add_argument("-f", "--format", help = "set format of output")
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()

"""
