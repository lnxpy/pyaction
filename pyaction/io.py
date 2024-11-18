import os

from pyaction.exceptions import WorkflowParameterNotFound
from pyaction.utils import get_running_platform
from pyaction.workflow.stream import WorkflowContext, push_to_local, push_to_runner


def write(context: WorkflowContext) -> None:
    """
    Writes the context to a stream based on the action running platform.

    Args:
        context (WorkflowContext): The context to be written.
    """
    if platform := get_running_platform():
        push_to_runner(context, stream=platform)
    else:
        push_to_local(context)


def read(param: str) -> str:
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
