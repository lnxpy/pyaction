import inspect
from typing import Callable, Dict

from pyaction import io


class PyAction:
    @staticmethod
    def action(func: Callable):
        """action decorator

        Args:
            func (Callable): action function

        Examples:
            In the `main.py` file, use this decorator to define your action like this:

            >>> workflow = PyAction()
            >>> @workflow.action
            >>> def my_action(...): ...

            Define your action input parameters as the `my_action` arguments.

            >>> ...
            >>> def my_action(name: str, age: int): ...
        """

        def wrapper():
            sig = inspect.signature(func)
            param_names = list(sig.parameters.keys())
            param_values = [io.read(param) for param in param_names]
            return func(*param_values)

        return wrapper()

    @staticmethod
    def write(context: Dict[str, str]) -> None:
        """writes the `context` env var(s) into the workflow environment

        Args:
            context (Dict[str, str]): variables and values
        """

        io.write(context)
