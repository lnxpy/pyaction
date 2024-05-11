from typing import Callable, Dict, get_type_hints

from pydantic import TypeAdapter

from pyaction import io
from pyaction.utils import check_parameters


class PyAction:
    @staticmethod
    def action() -> Callable:
        """action decorator

        Examples:
            use this action decorator in the following way:

            >>> workflow = PyAction()
            >>> @workflow.action()
            >>> def your_action(): ...

            you should define your action input parameters as the arguments of your function..

            >>> @workflow.action()
            >>> def your_action(name: str, age: int, is_student: bool): ...

        Returns:
            Callable: the wrapper action
        """

        def wrapper(func: Callable):
            check_parameters(func)
            params = {
                key: (type_, io.read(key))
                for key, type_ in get_type_hints(func).items()
                if key != "return"
            }

            retyped_params = {}

            for key, item in params.items():
                retyped_params[key] = TypeAdapter(item[0]).validate_python(item[1])

            return func(**retyped_params)

        return wrapper

    @staticmethod
    def write(context: Dict[str, str]) -> None:
        """writes the `context` env var(s) into the streamline

        Args:
            context (Dict[str, str]): variables and values
        """

        io.write(context)  # pragma: no cover
