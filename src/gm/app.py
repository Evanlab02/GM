"""Entry module for the CLI script."""

import sys

from gm.data import init


def main() -> int:
    """Entry point for the CLI script."""
    no_failures = init()
    if no_failures is False:
        return 1
    return 0


if __name__ == "__main__":
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
