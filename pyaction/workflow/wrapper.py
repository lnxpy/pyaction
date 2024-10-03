import subprocess
from typing import Any, Callable, Dict, get_type_hints

from pydantic import TypeAdapter

from pyaction import io
from pyaction.consts import DEBUG_MODE, Color
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

    def error(self, title: str) -> None:
        """pops an error annotation

        Args:
            title (str): the error title
        """

        if DEBUG_MODE:
            message = f"{Color.BOLD_RED.value}Error: {Color.RESET.value}{title}"
        else:
            message = f"::error::{title}"

        subprocess.call(["echo", message])

    def warning(self, title: str) -> None:
        """pops a warning annotation

        Args:
            title (str): the warning title
        """

        if DEBUG_MODE:
            message = f"{Color.YELLOW.value}Warning: {Color.RESET.value}{title}"
        else:
            message = f"::warning::{title}"

        subprocess.call(["echo", message])

    def notice(self, title: str) -> None:
        """pops a notice annotation

        Args:
            title (str): the notice title
        """

        if DEBUG_MODE:
            message = f"{Color.GREY.value}Notice: {Color.RESET.value}{title}"
        else:
            message = f"::notice::{title}"

        subprocess.call(["echo", message])
