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
