import inspect
import os
from typing import Callable, Optional

from pyaction.exceptions import NotAnnotated
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


def get_running_platform() -> Optional[str]:
    """
    Determine the current operating environment for the action.

    Returns:
        Returns the value stored in the `GITHUB_OUTPUT` environment variable if the action is running on Runner; otherwise, returns `None`.
    """
    return os.environ.get("GITHUB_OUTPUT", None)
