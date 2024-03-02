import os
from typing import Dict

BUFFER_PATH = os.environ["GITHUB_OUTPUT"]


def write(context: Dict[str, str]) -> None:
    """writes the key(s) (as variables) and value(s) (as values) to the output buffer

    Args:
        context: variables and values

    Examples:
        In your project, use this function like:

        >>> write_to_output({"name": "John", ...})

        ``name`` will be the variable name and ``John`` is the value.
    """

    with open(BUFFER_PATH, "a") as _buffer:
        for var, val in context.items():
            _buffer.write(f"{var}={val}\r\n")


def read(var: str) -> str | int | bool:
    """reads a variable from the inputs

    Args:
        var (str): variable name

    Returns:
        str | int | bool: value of `var`
    """

    prefix = "INPUT_"
    value = os.environ.get(prefix + var.upper(), "")

    return value
