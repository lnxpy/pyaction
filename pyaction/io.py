from __future__ import annotations

import os
from contextlib import nullcontext
from io import TextIOWrapper

from pyaction.consts import GITHUB_OUTPUT
from pyaction.exceptions import WorkflowParameterNotFound


def write(context: dict[str, str], stream: str | TextIOWrapper = GITHUB_OUTPUT) -> None:
    """writes the key(s) (as variables) and value(s) (as values) to the output stream

    Args:
        context (dict[str, str]): variables and values
        stream (str, TextIOWrapper): output stream (set to STDOUT locally and `GITHUB_OUTPUT` on production)

    Examples:
        In your action, use this function like:

        >>> write({"name": "John", "age": 20, ...})

        `name` and `age` are the variables and `John` and `20` are the values.
    """

    with nullcontext(stream) if isinstance(stream, TextIOWrapper) else open(
        stream, "w+"
    ) as streamline:
        for var, val in context.items():
            streamline.write(f"{var}={val}\r\n")


def read(param: str) -> str | int | bool | None:
    """reads a parameter from the inputs

    Args:
        param (str): parameter name

    Raises:
        WorkflowParameterNotFound: if the `param` is missing

    Returns:
        str | int | bool | None: value of `param`
    """

    prefix = "INPUT_"
    var_name = prefix + param.upper()

    try:
        value = os.environ[var_name]
    except KeyError:
        raise WorkflowParameterNotFound(
            f"Couldn't read the `{var_name}` input parameter from your pipeline. "
            "Make sure it's declared properly."
        )

    return value
