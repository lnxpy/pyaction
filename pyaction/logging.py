import sys
from typing import Dict

COLORS: Dict[str, str] = {
    "DEBUG": "\033[1m\033[94m",
    "INFO": "\033[1m\033[92m",
    "WARNING": "\033[1m\033[93m",
    "ERROR": "\033[1m\033[91m",
    "CRITICAL": "\033[1m\033[95m",
    "RESET": "\033[0m",
}


class Logger:
    def __init__(self, name: str = __name__, include_name: bool = True) -> None:
        """
        Initialize the Logger instance.

        Args:
            name (str): The name of the Logger (default is the current module's name).
            include_name (bool): Boolean flag to include the logger's name in the log output (default is True).
        """
        self.name: str = name
        self.include_name: bool = include_name

    def _log(self, level: str, message: str) -> None:
        """
        Log a message with the specified level.

        Args:
            level (str): The level of the log message (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
            message (str): The message to be logged.
        """
        color: str = COLORS.get(level, COLORS["RESET"])
        name: str = " - " + self.name if self.include_name else ""
        sys.stdout.write(f"{color}{level}{COLORS['RESET']}{name} - {message}\n")

    def debug(self, message: str) -> None:
        """
        Log a debug message.

        Args:
            message (str): The message to be logged.
        """
        self._log("DEBUG", message)

    def info(self, message: str) -> None:
        """
        Log an info message.

        Args:
            message (str): The message to be logged.
        """
        self._log("INFO", message)

    def warning(self, message: str) -> None:
        """
        Log a warning message.

        Args:
            message (str): The message to be logged.
        """
        self._log("WARNING", message)

    def error(self, message: str) -> None:
        """
        Log an error message.

        Args:
            message (str): The message to be logged.
        """
        self._log("ERROR", message)

    def critical(self, message: str) -> None:
        """
        Log a critical message.

        Args:
            message (str): The message to be logged.
        """
        self._log("CRITICAL", message)
