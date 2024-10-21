"""Contains the backup typer CLI."""

from typer import Typer

from gm.data.backup import BackupRepository
from gm.services.backup import BackupService

repo = BackupRepository()
service = BackupService(repo=repo)

cli = Typer(help="Manage backups.", no_args_is_help=True)


@cli.command()
def create() -> None:
    """Backs up all files locally. Useful when upgrading or developing."""
    service.backup()
