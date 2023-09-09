import os
from typing import Dict

BUFFER_PATH = os.environ["GITHUB_OUTPUT"]


def write_to_output(context: Dict[str, str]) -> None:
    """writes the keys (as variables) and values (as values) to the output buffer

    Args:
        context: variables and values

    Examples:
        In your project, use this function like:

        >>> write_to_output({"name": "John", ...})

        ``name`` will be the variable name and ``John`` is its value.
    """

    with open(BUFFER_PATH, "a") as _buffer:
        for var, val in context.items():
            _buffer.write(f"{var}={val}\r\n")
