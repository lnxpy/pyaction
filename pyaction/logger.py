import logging

from pyaction.consts import Color


class ColoredFormatter(logging.Formatter):
    format = "%(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: Color.GREY.value + format + Color.RESET.value,
        logging.INFO: Color.GREY.value + format + Color.RESET.value,
        logging.WARNING: Color.YELLOW.value + format + Color.RESET.value,
        logging.ERROR: Color.RED.value + format + Color.RESET.value,
        logging.CRITICAL: Color.BOLD_RED.value + format + Color.RESET.value,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(namespace: str = "pyaction") -> logging.Logger:
    """logger creator

    Args:
        namespace (str, optional): namespace of the module. Defaults to "pyaction"

    Returns:
        logging.Logger: logger object
    """
    logger = logging.getLogger(namespace)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    console_handler.setFormatter(ColoredFormatter())

    logger.addHandler(console_handler)

    return logger
