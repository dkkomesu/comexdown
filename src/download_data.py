import argparse

import download


def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("years", action="store", nargs="+")

    return parser


def expand_years(args):
    years = []
    for arg in args:
        if ":" in arg:
            start, end = arg.split(":")
            start, end = int(start), int(end)
            years += list(range(start, end + 1))
        else:
            years.append(int(arg))

    return years


def main():
    parser = set_parser()
    args = parser.parse_args()
    args = expand_years(args.years)

    for y in args:
        download.exp(y)
        download.imp(y)


if __name__ == '__main__':
    main()
