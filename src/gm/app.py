"""Entry module for the CLI script."""

import sys

from rich.console import Console
from rich.table import Table
from typer import Option, Typer
from typing_extensions import Annotated

from gm.cli.backup import cli as backup_cli
from gm.cli.mw3 import cli as mw3_cli
from gm.constants import SLUGS
from gm.data import init
from gm.data.base import get_current_slugs

console = Console()
cli = Typer(no_args_is_help=True)
cli.add_typer(backup_cli, name="backup")
cli.add_typer(mw3_cli, name="MW3")


@cli.command()
def slugs(
    current: Annotated[bool, Option(help="Display currently installed slugs.")] = False,
) -> None:
    """Display all slugs."""
    slugs = get_current_slugs() if current else SLUGS
    table = Table(show_header=True, header_style="bold")
    table.add_column("Slug", style="cyan")
    table.add_column("Name")
    table.add_column("File")
    for key, value in slugs.items():
        table.add_row(key, value.get("name"), value.get("file"))
    console.print(table)


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
