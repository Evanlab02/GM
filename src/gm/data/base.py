"""TODO."""

import json
import os
import sys

from rich import print as rprint

from gm.constants import SLUGS
from gm.constants.data import FULL_STORAGE_DIR, SLUG_FILE
from gm.logs.common import generic_error


def create_storage_folder() -> bool:
    """
    Create the storage folder for the application if it does not exist.

    Returns:
        Result (bool): The result of creating the storage folder, returns true if no errors.
    """
    if os.path.exists(FULL_STORAGE_DIR):
        return True

    rprint("Setting up storage...")
    try:
        os.makedirs(FULL_STORAGE_DIR)
    except OSError:
        generic_error(code=1)
        return False
    except Exception:
        generic_error(code=2)
        return False

    return True


def get_current_slugs() -> dict[str, str]:
    """
    Get the currently installed slugs.

    Returns:
        Slugs (dict[str, str]): The currently installed slugs.
    """
    if not os.path.exists(SLUG_FILE):
        return {}

    try:
        with open(SLUG_FILE, "r+", encoding="UTF-8") as file:
            return json.load(file)  # type: ignore
    except FileNotFoundError:
        generic_error(code=5)
    except json.JSONDecodeError:
        generic_error(code=6)
    except Exception:
        generic_error(code=7)
    sys.exit(1)


def create_slug_file() -> bool:
    """
    Creates/updates the slug file.

    Returns:
        Result (bool): The result of creating the slug file, returns true if no errors.
    """
    current_slugs = get_current_slugs()
    if current_slugs == SLUGS:
        return True

    rprint("Installing/updating slug file...")
    try:
        with open(SLUG_FILE, "w+", encoding="UTF-8") as file:
            json.dump(SLUGS, file, indent=4)
    except FileNotFoundError:
        generic_error(code=3)
    except Exception:
        generic_error(code=4)

    return True
