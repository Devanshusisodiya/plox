import sys
from plox.scanner import Plox

def main():
    plox = Plox()
    plox.main(args=sys.argv[1:])


if __name__ == "__main__":
    main()
