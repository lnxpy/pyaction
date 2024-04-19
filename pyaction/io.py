import os
from typing import Dict

from pyaction.consts import GITHUB_OUTPUT
from pyaction.exceptions import WorkflowParameterNotFound


def write(context: Dict[str, str]) -> None:
    """writes the key(s) (as variables) and value(s) (as values) to the output env variable

    Args:
        context: variables and values

    Examples:
        In your project, use this function like:

        >>> write({"name": "John", "age": 20, ...})

        `name` will be the variable name and `John` is the value.
    """

    with open(GITHUB_OUTPUT, "a") as _env:
        for var, val in context.items():
            _env.write(f"{var}={val}\r\n")


def read(param: str) -> str | int | bool | None:
    """reads a parameter from the inputs

    Args:
        param (str): parameter name

    Returns:
        str | int | bool: value of `param`
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
