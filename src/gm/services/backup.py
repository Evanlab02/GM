"""TODO."""

from rich import print as rprint

from gm.constants.data import PATH_MAP
from gm.data.interfaces.backup import IBackupRepository
from gm.services.interfaces.backup import IBackupService


class BackupService(IBackupService):
    """TODO."""

    def __init__(self, repo: IBackupRepository) -> None:
        """TODO."""
        self.repo = repo

    def backup(self) -> tuple[int, int]:
        """
        Backup all app files.

        Returns:
            Result (tuple[int, int]): The number of successful and failed backups.
        """
        self.repo.create_backup_storage()
        for current, backup in PATH_MAP.items():
            rprint(f"[bold cyan][PROCESSING][/bold cyan] {current}")
            result = self.repo.backup(current, backup)
            if result == 0:
                rprint(f"[bold green][DONE][/bold green] {backup}")
            elif result == 1:
                rprint(f"[bold yellow][SKIPPED][/bold yellow] {backup}")
            else:
                rprint(f"[bold red][ERROR][/bold red] {backup}")

        return 0, 0
