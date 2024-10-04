import subprocess

from pyaction.consts import DEBUG_MODE, Color


def error(title: str) -> None:
    """pops an error annotation

    Args:
        title (str): the error title
    """

    if DEBUG_MODE:
        message = f"{Color.BOLD_RED.value}Error: {Color.RESET.value}{title}"
    else:
        message = f"::error::{title}"

    subprocess.call(["echo", message])


def warning(title: str) -> None:
    """pops a warning annotation

    Args:
        title (str): the warning title
    """

    if DEBUG_MODE:
        message = f"{Color.YELLOW.value}Warning: {Color.RESET.value}{title}"
    else:
        message = f"::warning::{title}"

    subprocess.call(["echo", message])


def notice(title: str) -> None:
    """pops a notice annotation

    Args:
        title (str): the notice title
    """

    if DEBUG_MODE:
        message = f"{Color.GREY.value}Notice: {Color.RESET.value}{title}"
    else:
        message = f"::notice::{title}"

    subprocess.call(["echo", message])
