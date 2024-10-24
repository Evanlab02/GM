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

    def backup(self) -> tuple[int, int, int]:
        """
        Backup all app files.

        Returns:
            Result (tuple[int, int, int]): The number of successful, skipped and failed backups.
        """
        success = 0
        skipped = 0
        failed = 0

        self.repo.create_backup_storage()
        for current, backup in PATH_MAP.items():
            result = self.repo.load(current, backup)
            if result == 0:
                success += 1
                rprint(f"[bold green][DONE][/bold green] {backup}")
            elif result == 1:
                skipped += 1
                rprint(f"[bold yellow][SKIPPED][/bold yellow] {backup}")
            else:
                failed += 1
                rprint(f"[bold red][ERROR][/bold red] {backup}")

        return success, skipped, failed

    def load(self) -> tuple[int, int, int]:
        """
        Load all app files from backup to primary storage.

        Returns:
            Result (tuple[int, int, int]): The number of successful, skipped and failed imports.
        """
        success = 0
        skipped = 0
        failed = 0

        for current, backup in PATH_MAP.items():
            result = self.repo.load(backup, current)
            if result == 0:
                success += 1
                rprint(f"[bold green][DONE][/bold green] {current}")
            elif result == 1:
                skipped += 1
                rprint(f"[bold yellow][SKIPPED][/bold yellow] {current}")
            else:
                failed += 1
                rprint(f"[bold red][ERROR][/bold red] {current}")

        return success, skipped, failed
