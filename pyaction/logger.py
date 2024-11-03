import logging
from typing import TypeAlias

from pyaction.consts import Color

LoggerFormat: TypeAlias = str


class ColoredFormatter(logging.Formatter):
    base_format: LoggerFormat = "%(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: Color.GREY.value + base_format + Color.RESET.value,
        logging.INFO: Color.GREY.value + base_format + Color.RESET.value,
        logging.WARNING: Color.YELLOW.value + base_format + Color.RESET.value,
        logging.ERROR: Color.RED.value + base_format + Color.RESET.value,
        logging.CRITICAL: Color.BOLD_RED.value + base_format + Color.RESET.value,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno, self.base_format)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(namespace: str = "pyaction") -> logging.Logger:
    """logger creator

    Args:
        namespace (str, optional): namespace of the module. Defaults to "pyaction".

    Returns:
        logging.Logger: Configured logger object.
    """

    logger = logging.getLogger(namespace)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(ColoredFormatter())

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
