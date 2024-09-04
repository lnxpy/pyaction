import os
from typing import Any, Dict

from pyaction.consts import DEBUG_MODE, GITHUB_OUTPUT
from pyaction.exceptions import WorkflowParameterNotFound
from pyaction.workflow.stream import LocalStream, WorkflowStream


def write(context: Dict[str, Any], stream: str = None) -> None:
    """writes the key(s) (as variables) and value(s) (as values) into the output stream

    Args:
        context (Dict[str, Any]): variables and values
        stream (str, optional): output stream Defaults to None.

    """

    if DEBUG_MODE:
        LocalStream().put(context)
    else:
        WorkflowStream(stream or GITHUB_OUTPUT).put(context)


def read(param: str) -> str:
    """reads a parameter from the inputs

    Args:
        param (str): parameter name

    Raises:
        WorkflowParameterNotFound: if the `param` is missing

    Returns:
        str: value of `param`
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
