import inspect
from typing import Callable

from rich.table import Table

from pyaction.exceptions import NotAnnotated
from pyaction.logger import setup_logger

logger = setup_logger(__name__)


def check_parameters(func: Callable) -> None:
    """checks the function params annotations and default values

    Args:
        func (Callable): the function

    Raises:
        NotAnnotated: if there is param(s) not annotated
    """

    signature = inspect.signature(func)
    for param_name, param in signature.parameters.items():
        if param.default != inspect.Parameter.empty:
            logger.warning(
                f"Parameter `{param_name}` in the action function `{func.__name__}` has gotten the default value `{param.default}` which has no effect. "
                "Set the default value(s) inside the `action.yml` instead."
            )

        if param.annotation == inspect.Parameter.empty:
            raise NotAnnotated(
                f"Parameter `{param_name}` in the action function `{func.__name__}` is not annotated."
            )


def create_output_table() -> Table:
    """returns a `rich.Table` output table

    Returns:
        Table: rich table with static columns
    """

    table = Table(show_lines=True)

    table.add_column(
        "Variable",
        justify="center",
        style="blue bold",
        vertical="middle",
    )
    table.add_column(
        "Value",
        justify="center",
        style="green",
        vertical="middle",
    )
    table.add_column(
        "Type",
        justify="center",
        style="rgb(249,38,114) italic",
        vertical="middle",
    )
    table.add_column(
        "Workflow Usage",
        justify="center",
        style="magenta",
        vertical="middle",
    )

    return table
