import os
from typing import Dict

from pyaction.exceptions import WorkflowParameterNotFound

BUFFER_PATH = os.environ.get("GITHUB_OUTPUT", os.devnull)


def write(context: Dict[str, str]) -> None:
    """writes the key(s) (as variables) and value(s) (as values) to the output buffer

    Args:
        context: variables and values

    Examples:
        In your project, use this function like:

        >>> write({"name": "John", "age": 20, ...})

        `name` will be the variable name and `John` is the value.
    """

    with open(BUFFER_PATH, "a") as _buffer:
        for var, val in context.items():
            _buffer.write(f"{var}={val}\r\n")


def read(param: str) -> str | int | bool | None:
    """reads a parameter from the inputs

    Args:
        param (str): parameter name

    Returns:
        str | int | bool: value of `param`
    """

    prefix = "INPUT_"

    try:
        value = os.environ[prefix + param.upper()]
    except KeyError:
        raise WorkflowParameterNotFound(
            f"Couldn't read the `{param}` input parameter from your pipeline. "
            "Make sure it's declared properly."
        )

    return value
