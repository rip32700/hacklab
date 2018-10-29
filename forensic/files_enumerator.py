
import os
import argparse


root_dir = None
types = None


def parse_args():
    global root_dir, types
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='directory to search', required=True)
    parser.add_argument('-t', '--types', help='types to search to search')
    args = parser.parse_args()
    root_dir = args.dir
    if args.types:
        types = args.types.split(',')


def main():
    global root_dir, types
    parse_args()
    base_pre_fix = len(root_dir.split(os.sep)) - 1
    for root, dirs, files in os.walk(root_dir):
        path = root.split(os.sep)
        print((len(path) - 1 - base_pre_fix) * '---', os.path.basename(root))
        for file in files:
            if types is not None:
                suffix = file.split('.')[-1]
                if suffix in types:
                    print((len(path) - base_pre_fix) * '---', file)
            else:
                print((len(path) - base_pre_fix) * '---', file)


if __name__ == "__main__":
    main()
