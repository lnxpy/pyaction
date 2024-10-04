from typing import Any, Callable, Dict, get_type_hints

from pydantic import TypeAdapter

from pyaction import io
from pyaction.utils import check_parameters


class Action:
    def __call__(self, func: Callable) -> Any:
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


class PyAction:
    def __init__(self) -> None:
        self.action = Action

    @staticmethod
    def write(context: Dict[str, Any]) -> None:
        """writes the `context` env var(s) into the streamline

        Args:
            context (Dict[str, Any]): variables and values
        """

        io.write(context)  # pragma: no cover
