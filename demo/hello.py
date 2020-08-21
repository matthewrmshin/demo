"""Classic starter application."""

import sys


def main():
    """Classic starter program."""
    who = 'World'
    if sys.argv[1:] and sys.argv[1]:
        who = sys.argv[1]
    print(f'Hello {who}!')


if __name__ == '__main__':
    main()
