import sys
from typing import Callable, get_type_hints

from pydantic import TypeAdapter

from pyaction.exceptions import NotAnnotated
from pyaction.logging import Logger
from pyaction.utils import get_running_platform
from pyaction.workflow.stream import WorkflowContext, push_to_local, push_to_runner
from pyaction.workflow.utils import check_parameters, read_input_parameter

logger = Logger(__name__, include_name=False)


class PyAction:
    def action(self, func: Callable):
        def wrapper(*args, **kwargs):
            try:
                # Validate parameter annotations
                check_parameters(func)
            except NotAnnotated as e:
                logger.error(f"Parameter validation error: {e}")
                sys.exit(1)

            # Extract parameter types and values
            param_hints = get_type_hints(func)
            params = {
                key: (type_, read_input_parameter(key))
                for key, type_ in param_hints.items()
                if key != "return"
            }

            # Validate and retype parameters
            try:
                retyped_params = {
                    key: TypeAdapter(type_).validate_python(value)
                    for key, (type_, value) in params.items()
                }
            except Exception as e:
                logger.error(f"Parameter type validation error: {e}")
                sys.exit(1)

            # Execute the function with retyped parameters
            func(**retyped_params)

        # Execute the wrapper immediately
        wrapper()
        return func

    @staticmethod
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
