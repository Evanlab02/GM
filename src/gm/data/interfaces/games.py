"""TODO."""

from abc import ABC, abstractmethod


class IGamesRepository(ABC):
    """TODO."""

    @abstractmethod
    def install(self, slug: str, data: dict) -> None:  # type: ignore
        """Create the game file, if it does not exist."""

    @abstractmethod
    def save(self, slug: str, data: dict) -> None:  # type: ignore
        """Save to the game file."""

    @abstractmethod
    def load(self, slug: str) -> dict:  # type: ignore
        """
        Load the game file, if it exists.

        Returns:
            Result (dict): The data from the file.
        """
