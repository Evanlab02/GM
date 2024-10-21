"""TODO."""

from abc import ABC, abstractmethod


class IBackupRepository(ABC):
    """TODO."""

    @abstractmethod
    def create_backup_storage(self) -> bool:
        """
        Create the storage folder for the application if it does not exist.

        Returns:
            Result (bool): The result of creating the storage folder, returns true if no errors.
        """

    @abstractmethod
    def backup(self, original: str, new: str) -> int:
        """
        Backup files to the given path.

        Args:
            original (str): Original file path.
            new (str): The new file path for the backup.

        Returns:
            Result (bool): The result of the backup.
        """
