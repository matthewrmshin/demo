"""Classic starter application."""


def get_hello(who=None):
    """Classic starter program."""
    if not who:
        who = 'World'
    return f'Hello and hi, {who}!'


def main():
    """Classic starter program."""
    print(get_hello())


if __name__ == '__main__':
    main()
