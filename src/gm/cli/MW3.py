"""Contains the MW3 typer CLI."""

from rich.console import Console
from rich.table import Table
from typer import Option, Typer
from typing_extensions import Annotated

from gm.data.games import GamesRepository
from gm.schemas.MW3 import MW3
from gm.services.MW3 import MW3Service
from gm.utils.MW3 import print_account_info

console = Console()
repo = GamesRepository()
service = MW3Service()

cli = Typer(help="Manage your Call of Duty MW3 progress. [BETA]", no_args_is_help=True)


@cli.command()
def install() -> None:
    """Install the files for Call of Duty MW3."""
    repo.install("MW3", MW3().model_dump())


@cli.command()
def account() -> None:
    """View all account information."""
    data = service.account()
    print_account_info(data=data)


@cli.command()
def level(
    inc: Annotated[int, Option(help="Increment your level by this amount.")] = 1,
    value: Annotated[
        int | None, Option(help="Directly set the account level to this value.")
    ] = None,
) -> None:
    """Level your account."""
    old, new = service.level(inc=inc, value=value)

    if value:
        inc = new - old

    table = Table(show_header=True, header_style="bold")
    table.title = "Account Information"
    table.title_justify = "center"
    table.title_style = "bold"
    table.add_column("Old")
    table.add_column("Update")
    table.add_column("New", style="green")
    table.add_row(str(old), f"{old} + {inc}", str(new))
    table.caption = f"Account level: {new}"
    console.print(table)
