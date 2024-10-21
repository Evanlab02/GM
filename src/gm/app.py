"""Entry module for the CLI script."""

import sys

from typer import Typer

from gm.cli.backup import cli as backup_cli
from gm.data import init

cli = Typer(no_args_is_help=True)
cli.add_typer(backup_cli, name="backup")


def main() -> int:
    """Entry point for the CLI script."""
    no_failures = init()
    if no_failures is False:
        return 1
    cli()
    return 0


if __name__ == "__main__":
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
