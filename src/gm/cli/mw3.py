"""Contains the MW3 typer CLI."""

from rich.console import Console
from typer import Typer

from gm.schemas.mw3 import MW3
from gm.data.games import GamesRepository
from gm.services.mw3 import MW3Service

console = Console()
repo = GamesRepository()
service = MW3Service()

cli = Typer(help="Manage your Call of Duty MW3 progress.", no_args_is_help=True)


@cli.command()
def install() -> None:
    """Install the files for Call of Duty MW3."""
    repo.install("MW3", MW3().model_dump())


@cli.command()
def level() -> None:
    """Level your account."""
    service.level()
