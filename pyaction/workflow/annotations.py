from __future__ import annotations

import subprocess

from pyaction.utils import get_running_platform

RUNNING_ON_RUNNER: bool = bool(get_running_platform())

# escaping rules, as documented in the GitHub workflow-commands reference
_DATA_ESCAPES: dict[str, str] = {"%": "%25", "\r": "%0D", "\n": "%0A"}
_DELIMITER_ESCAPES: dict[str, str] = {**_DATA_ESCAPES, ":": "%3A", ",": "%2C"}


def _escape(value: str | int, escapes: dict[str, str]) -> str:
    """Escapes a value according to the given escaping rules."""
    text = str(value)
    for character, code in escapes.items():
        text = text.replace(character, code)
    return text


def _pop(
    command: str,
    message: str,
    *,
    title: str | None = None,
    file: str | None = None,
    line: int | None = None,
    end_line: int | None = None,
    col: int | None = None,
    end_column: int | None = None,
) -> None:
    """Builds and pops a workflow-command annotation."""
    properties = []
    if title is not None:
        properties.append(f"title={_escape(title, _DELIMITER_ESCAPES)}")
    if file is not None:
        properties.append(f"file={_escape(file, _DELIMITER_ESCAPES)}")
    if line is not None:
        properties.append(f"line={_escape(line, _DATA_ESCAPES)}")
    if end_line is not None:
        properties.append(f"endLine={_escape(end_line, _DATA_ESCAPES)}")
    if col is not None:
        properties.append(f"col={_escape(col, _DATA_ESCAPES)}")
    if end_column is not None:
        properties.append(f"endColumn={_escape(end_column, _DATA_ESCAPES)}")

    if RUNNING_ON_RUNNER:
        metadata = ""
        if properties:
            metadata = " " + ",".join(properties)
        output = f"::{command}{metadata}::{_escape(message, _DATA_ESCAPES)}"
    else:
        output = f"{command.capitalize()} Annotation: {message}"

    subprocess.call(["echo", output])


def error(
    message: str,
    *,
    title: str | None = None,
    file: str | None = None,
    line: int | None = None,
    end_line: int | None = None,
    col: int | None = None,
    end_column: int | None = None,
) -> None:
    """
    Pops an error annotation.

    Args:
        message (str): The error message.
        title (str): A custom title displayed above the annotation.
        file (str): The filename the annotation is associated with.
        line (int): The starting line number (starting at 1).
        end_line (int): The ending line number.
        col (int): The starting column number (starting at 1).
        end_column (int): The ending column number.
    """

    _pop(
        "error",
        message,
        title=title,
        file=file,
        line=line,
        end_line=end_line,
        col=col,
        end_column=end_column,
    )


def warning(
    message: str,
    *,
    title: str | None = None,
    file: str | None = None,
    line: int | None = None,
    end_line: int | None = None,
    col: int | None = None,
    end_column: int | None = None,
) -> None:
    """
    Pops a warning annotation.

    Args:
        message (str): The warning message.
        title (str): A custom title displayed above the annotation.
        file (str): The filename the annotation is associated with.
        line (int): The starting line number (starting at 1).
        end_line (int): The ending line number.
        col (int): The starting column number (starting at 1).
        end_column (int): The ending column number.
    """

    _pop(
        "warning",
        message,
        title=title,
        file=file,
        line=line,
        end_line=end_line,
        col=col,
        end_column=end_column,
    )


def notice(
    message: str,
    *,
    title: str | None = None,
    file: str | None = None,
    line: int | None = None,
    end_line: int | None = None,
    col: int | None = None,
    end_column: int | None = None,
) -> None:
    """
    Pops a notice annotation.

    Args:
        message (str): The notice message.
        title (str): A custom title displayed above the annotation.
        file (str): The filename the annotation is associated with.
        line (int): The starting line number (starting at 1).
        end_line (int): The ending line number.
        col (int): The starting column number (starting at 1).
        end_column (int): The ending column number.
    """

    _pop(
        "notice",
        message,
        title=title,
        file=file,
        line=line,
        end_line=end_line,
        col=col,
        end_column=end_column,
    )
