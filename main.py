import sys

from plox.plox import Plox


def main():
    plox = Plox()
    plox.main(args=sys.argv[1:])


if __name__ == "__main__":
    main()
