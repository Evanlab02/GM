"""TODO."""

import json
import os

from rich import print as rprint

from gm.constants.data import FULL_BACKUP_DIR
from gm.data.interfaces.backup import IBackupRepository
from gm.logs.common import generic_error


class BackupRepository(IBackupRepository):
    """TODO."""

    def create_backup_storage(self) -> bool:
        """
        Create the storage folder for the application if it does not exist.

        Returns:
            Result (bool): The result of creating the storage folder, returns true if no errors.
        """
        if os.path.exists(FULL_BACKUP_DIR):
            return True

        rprint("[bold cyan][INFO][/bold cyan] Setting up backup storage...")
        try:
            os.makedirs(FULL_BACKUP_DIR)
        except OSError:
            generic_error(code=1)
            return False
        except Exception:
            generic_error(code=2)
            return False

        return True

    def backup(self, original: str, new: str) -> int:
        """
        Backup files to the given path.

        Args:
            original (str): Original file path.
            new (str): The new file path for the backup.

        Returns:
            Result (int): The result of the backup.
        """
        if not os.path.exists(original):
            return 1

        try:
            with open(original, "r", encoding="UTF-8") as file:
                data = json.load(file)

            with open(new, "w+", encoding="UTF-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            rprint(e)
            return 2

        return 0

    def load(self, backup: str, original: str) -> int:
        """
        Load file to the primary storage.

        Args:
            backup (str): Backup file path.
            new (str): The primary storage file path.

        Returns:
            Result (int): The result of the import.
        """
        if not os.path.exists(backup):
            return 1

        try:
            with open(backup, "r", encoding="UTF-8") as file:
                data = json.load(file)

            with open(original, "w+", encoding="UTF-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            rprint(e)
            return 2

        return 0
