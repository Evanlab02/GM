"""TODO."""

from abc import ABC, abstractmethod


class IGamesRepository(ABC):
    """TODO."""

    @abstractmethod
    def install(self, slug: str) -> bool:
        """
        Create the storage folder for the application if it does not exist.

        Returns:
            Result (bool): The result of creating the storage folder, returns true if no errors.
        """
