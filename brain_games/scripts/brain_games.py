#!/usr/bin/env python3
from ..cli import welcome_user


def main():
    name = welcome_user()
    parity_check()


if __name__ == '__main__':
    main()
