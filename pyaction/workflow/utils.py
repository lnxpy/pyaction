import inspect
import os
from typing import Callable

from pyaction.exceptions import NotAnnotated, WorkflowParameterNotFound
from pyaction.logging import Logger

logger = Logger(__name__, include_name=False)


def check_parameters(func: Callable) -> None:
    """
    Checks the function params typing and annotation.

    Args:
        func (Callable): The function.

    Raises:
        NotAnnotated: If there is param(s) not annotated.
    """
    signature = inspect.signature(func)
    for param_name, param in signature.parameters.items():
        if param.annotation == inspect.Parameter.empty:
            raise NotAnnotated(f"parameter `{param_name}` is not annotated.")

        if param.default != inspect.Parameter.empty:
            logger.warning(
                f"parameter `{param_name}` has a default value which has no effect. "
                "Set the default value(s) inside the `action.yml`."
            )


def read_input_parameter(param: str) -> str:
    """
    Reads a parameter from the inputs.

    Args:
        param (str): Parameter name

    Raises:
        WorkflowParameterNotFound: If the `param` is missing.

    Returns:
        str: Value of `param`.
    """
    prefix = "INPUT_"
    var_name = prefix + param.upper()

    try:
        value = os.environ[var_name]
    except KeyError:
        raise WorkflowParameterNotFound(
            f"unable to read the `{var_name}` parameter. "
            "Make sure it's declared properly."
        )

    return value
