"""TODO."""

from abc import ABC, abstractmethod
from typing import Any


class ICOD(ABC):
    """TODO."""

    def __init__(self) -> None:
        """TODO."""
        super().__init__()

    @abstractmethod
    def level(self, inc: int = 1, value: int | None = None) -> tuple[int, int]:
        """
        Level the account by the inc.

        Args:
            inc (int): Level the account by this inc.
            value (int optional): Directly set the account level to this value.

        Returns:
            results (tuple[int, int]): The previous level, and the new level.
        """

    @abstractmethod
    def level_weapon(
        self, category: str, key: str, inc: int = 1
    ) -> tuple[int, int, str]:
        """
        Level the weapon by the inc.

        Args:
            category (str): Level a weapon in this category.
            key (str): Level the weapon with this key.
            inc (int): Level the account by this inc.

        Returns:
            results (tuple[int, int, str]): The previous level, the new level and the weapon name.
        """

    @abstractmethod
    def account(self) -> Any:
        """
        Get all account information.

        Returns:
            result (Any): The full account details object.
        """
