"""Contains the backup typer CLI."""

from rich.console import Console
from rich.table import Table
from typer import Typer

from gm.data.backup import BackupRepository
from gm.services.backup import BackupService

console = Console()
repo = BackupRepository()
service = BackupService(repo=repo)

cli = Typer(help="Manage backups.", no_args_is_help=True)


def result_table(success: int, skipped: int, failed: int) -> None:
    """Print out a result table for the status of operations."""
    table = Table(show_header=True, header_style="bold")
    table.add_column("Success", style="green")
    table.add_column("Skipped", style="yellow")
    table.add_column("Failed", style="red", justify="right")
    table.add_row(str(success), str(skipped), str(failed))
    console.print(table)


@cli.command()
def create() -> None:
    """Backs up all files locally. Useful when upgrading or developing."""
    success, skipped, failed = service.backup()
    result_table(success=success, skipped=skipped, failed=failed)


@cli.command(name="import")
def load() -> None:
    """Import the backup files on the device into the default directory."""
    success, skipped, failed = service.load()
    result_table(success=success, skipped=skipped, failed=failed)
