"""TODO."""

from rich.table import Table
from rich.console import Console

from gm.schemas.MW3 import MW3


def print_account_info(data: MW3):
    """Print account info."""
    console = Console()
    table = Table(show_header=True, header_style="bold")
    table.title = "Account Information"
    table.title_justify = "center"
    table.title_style = "bold"

    table.add_column("Stat")
    table.add_column("Level")

    table.add_row("Account Level", f"[green]{data.level}[/green]")
    console.print(table)
