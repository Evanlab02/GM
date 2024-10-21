"""TODO"""

from gm.data.base import create_storage_folder, create_slug_file


def init() -> bool:
    """
    Create the initial slug file.

    Returns:
        Result (bool): The result of the initialization of the slug file.
    """
    no_failures = True

    no_failures = create_storage_folder()
    if no_failures is False:
        return False

    no_failures = create_slug_file()
    if no_failures is False:
        return False

    return True
