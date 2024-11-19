import subprocess

from pyaction.utils import get_running_platform

RUNNING_ON_RUNNER: bool = True if get_running_platform() else False


def error(title: str) -> None:
    """
    Pops an error annotation.

    Args:
        title (str): The error title.
    """

    if RUNNING_ON_RUNNER:
        message = f"::error::{title}"
    else:
        message = f"Error Annotation: {title}"

    subprocess.call(["echo", message])


def warning(title: str) -> None:
    """
    Pops a warning annotation.

    Args:
        title (str): The warning title.
    """

    if RUNNING_ON_RUNNER:
        message = f"::warning::{title}"
    else:
        message = f"Warning Annotation: {title}"

    subprocess.call(["echo", message])


def notice(title: str) -> None:
    """
    Pops a notice annotation.

    Args:
        title (str): The notice title.
    """

    if RUNNING_ON_RUNNER:
        message = f"::notice::{title}"
    else:
        message = f"Notice Annotation: {title}"

    subprocess.call(["echo", message])
