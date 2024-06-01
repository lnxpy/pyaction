from __future__ import annotations

import os
from contextlib import nullcontext
from io import TextIOWrapper

from rich.console import Console

from pyaction.consts import DEBUG_MODE, GITHUB_OUTPUT, MULTILINE_OUTPUT
from pyaction.exceptions import WorkflowParameterNotFound
from pyaction.utils import create_output_table


def write(context: dict[str, str], stream: str | TextIOWrapper = GITHUB_OUTPUT) -> None:
    """writes the key(s) (as variables) and value(s) (as values) into the output stream

    Args:
        context (dict[str, str]): variables and values
        stream (str, TextIOWrapper): output stream (set to STDOUT locally, but `GITHUB_OUTPUT` on cloud)
    """

    if DEBUG_MODE:
        table = create_output_table()
        console = Console()

        with nullcontext(stream) as streamline:
            for var, val in context.items():
                table.add_row(
                    var,
                    str(val),
                    str(type(val)),
                    f"${{{{ steps.STEP_ID.outputs.{var} }}}}",
                )

        console.print(table)
    else:
        with open(stream, "+w") as streamline:
            for var, val in context.items():
                if "\n" in val:
                    streamline.write(MULTILINE_OUTPUT.format(variable=var, value=val))
                else:
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
