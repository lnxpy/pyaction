import sys
from typing import Callable, get_type_hints

from pydantic import TypeAdapter

from pyaction import io
from pyaction.exceptions import NotAnnotated
from pyaction.logging import Logger
from pyaction.utils import check_parameters
from pyaction.workflow.stream import WorkflowContext

logger = Logger(__name__, include_name=False)


class Action:
    def __call__(self, func: Callable) -> None:
        """
        Validate parameters based on function annotations and process them accordingly.

        Args:
            func (Callable): The function to be executed with validated parameters.

        Raises:
            NotAnnotated: If function parameters are not annotated properly.

        Returns:
            The result of the function call with validated parameters.
        """
        try:
            check_parameters(func)
        except NotAnnotated as e:
            logger.error(str(e))
            sys.exit(1)

        params = {
            key: (type_, io.read(key))
            for key, type_ in get_type_hints(func).items()
            if key != "return"
        }

        retyped_params = {}

        for key, item in params.items():
            retyped_params[key] = TypeAdapter(item[0]).validate_python(item[1])

        return func(**retyped_params)


class PyAction:
    def __init__(self) -> None:
        """
        Initializes PyAction class with an instance of the Action class.
        """
        self.action = Action

    @staticmethod
    def write(context: WorkflowContext) -> None:
        """
        Writes the `context` env var(s) into the streamline.

        Args:
            context (WorkflowContext): Variables and values.
        """
        io.write(context)  # pragma: no cover
