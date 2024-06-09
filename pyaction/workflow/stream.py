from abc import ABC, abstractmethod
from typing import Any, Dict

from pyaction.consts import GITHUB_OUTPUT, MULTILINE_OUTPUT
from pyaction.workflow.consts import LOCAL_TABLE_COLS


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

        from rich.table import Table

        self.table = Table(show_lines=True)
        for col in LOCAL_TABLE_COLS:
            self.table.add_column(**col, justify="center", vertical="middle")

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
