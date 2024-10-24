"""TODO."""

from gm.data.games import GamesRepository
from gm.schemas.MW3 import MW3
from gm.services.interfaces.cod import ICOD


class MW3Service(ICOD):
    """TODO."""

    def __init__(self) -> None:
        """TODO."""
        self.repo = GamesRepository()
        super().__init__()

    def level(self, inc: int = 1, value: int | None = None) -> tuple[int, int]:
        """
        Level the account by the inc.

        Args:
            inc (int): Level the account by this inc.
            value (int optional): Directly set the account level to this value.

        Returns:
            results (tuple[int, int]): The previous level, and the new level.
        """
        data = self.repo.load("MW3")
        game_data = MW3.model_validate(data, strict=True)
        old = game_data.level

        if value:
            new = value
        else:
            new = game_data.level + inc

        game_data.level = new
        data = game_data.model_dump()
        self.repo.save("MW3", data)
        return old, new

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
        return 1, 1, ""

    def account(self) -> MW3:
        """
        Get all account information.

        Returns:
            result (MW3): The full account details object.
        """
        data = self.repo.load("MW3")
        game_data = MW3.model_validate(data, strict=True)
        return game_data
