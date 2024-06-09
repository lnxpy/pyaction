from abc import ABC, abstractmethod
from typing import Any, Dict

from pyaction.consts import GITHUB_OUTPUT, MULTILINE_OUTPUT
from pyaction.workflow.utils import generate_param_table


class Stream(ABC):
    @abstractmethod
    def put(self, context: Dict[str, Any]):
        pass


class LocalStream(Stream):
    def __init__(self) -> None:
        """initializer

        Args:
            context (Dict[str, Any]): context containing the variables
        """

        self.table = generate_param_table()

    def put(self, context: Dict[str, Any]):
        """uses `rich` to put the information into the STDOUT"""

        from rich.console import Console

        console = Console()

        for var, val in context.items():
            self.table.add_row(
                var,
                str(val),
                str(type(val)),
                f"${{{{ steps.STEP_ID.outputs.{var} }}}}",
            )

        console.print(self.table)


class WorkflowStream(Stream):
    def __init__(self, stream: str = GITHUB_OUTPUT) -> None:
        self.stream = stream

    def put(self, context: Dict[str, Any]):
        """writes the `context` into the `GITHUB_OUTPUT` environment variable"""

        with open(self.stream, "+w") as streamline:
            for var, val in context.items():
                if "\n" in val:
                    streamline.write(MULTILINE_OUTPUT.format(variable=var, value=val))
                else:
                    streamline.write(f"{var}={val}\r\n")
