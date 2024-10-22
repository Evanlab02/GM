"""TODO."""

from abc import ABC, abstractmethod

from gm.data.interfaces.backup import IBackupRepository


class IBackupService(ABC):
    """TODO."""

    def __init__(self, repo: IBackupRepository) -> None:
        """TODO."""
        self.repo = repo

    @abstractmethod
    def backup(self) -> tuple[int, int, int]:
        """
        Backup all app files.

        Returns:
            Result (tuple[int, int, int]): The number of successful, skipped and failed backups.
        """

    @abstractmethod
    def load(self) -> tuple[int, int, int]:
        """
        Load all app files from backup to primary storage.

        Returns:
            Result (tuple[int, int, int]): The number of successful, skipped and failed imports.
        """
