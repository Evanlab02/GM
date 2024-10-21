"""TODO"""

from rich import print as rprint

from gm.constants.github import REPOSITORY


def generic_error(code: int = 0) -> None:
    """Print out a generic error, for when things go wrong despite all your efforts."""
    rprint(f"[red]Something went very wrong! ({code})[/red]")
    rprint("What have you done?!")
    rprint(
        f"JK, if you are experiencing this issue, please open a issue on {REPOSITORY} with this message along with your system info."  # noqa
    )
