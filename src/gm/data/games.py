"""TODO."""

import json
import os
import sys

from rich import print as rprint

from gm.constants import SLUGS
from gm.constants.data import FULL_STORAGE_DIR
from gm.data.interfaces.games import IGamesRepository
from gm.logs.common import generic_error


class GamesRepository(IGamesRepository):
    """TODO."""

    def install(self, slug: str, data: dict) -> None:  # type: ignore
        """Create the game file, if it does not exist."""
        DATA = SLUGS.get(slug)
        if not DATA:
            generic_error(code=10)
            sys.exit(1)

        FILE_NAME = DATA.get("file")
        if not FILE_NAME:
            generic_error(code=9)
            sys.exit(1)

        FULL_FILE = os.path.join(FULL_STORAGE_DIR, FILE_NAME)
        if os.path.exists(FULL_FILE):
            return

        try:
            with open(FULL_FILE, "w+", encoding="UTF-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            generic_error(code=8)
            sys.exit(1)
        except Exception:
            generic_error(code=9)
            sys.exit(1)

        rprint(f"[bold green][DONE][/bold green] Installed {slug}.")

    def save(self, slug: str, data: dict) -> None:  # type: ignore
        """Save to the game file."""
        DATA = SLUGS.get(slug)
        if not DATA:
            generic_error(code=16)
            sys.exit(16)

        FILE_NAME = DATA.get("file")
        if not FILE_NAME:
            generic_error(code=16)
            sys.exit(17)

        FULL_FILE = os.path.join(FULL_STORAGE_DIR, FILE_NAME)

        if not os.path.exists(FULL_FILE):
            rprint(
                "[bold red][ERROR][/bold red] Please install the game files, and try again."
            )
            sys.exit(20)

        try:
            with open(FULL_FILE, "w+", encoding="UTF-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            generic_error(code=18)
            sys.exit(18)
        except Exception:
            generic_error(code=19)
            sys.exit(19)

    def load(self, slug: str) -> dict:  # type: ignore
        """
        Load the game file, if it exists.

        Returns:
            Result (dict): The data from the file.
        """
        DATA = SLUGS.get(slug)
        if not DATA:
            generic_error(code=11)
            sys.exit(11)

        FILE_NAME = DATA.get("file")
        if not FILE_NAME:
            generic_error(code=12)
            sys.exit(12)

        FULL_FILE = os.path.join(FULL_STORAGE_DIR, FILE_NAME)
        if not os.path.exists(FULL_FILE):
            generic_error(code=13)
            sys.exit(13)

        try:
            with open(FULL_FILE, "r+", encoding="UTF-8") as file:
                return json.load(file)  # type: ignore
        except FileNotFoundError:
            generic_error(code=14)
            sys.exit(14)
        except Exception:
            generic_error(code=15)
            sys.exit(15)
