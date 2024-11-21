from io import StringIO
from unittest.mock import patch

import pytest

from pyaction.logging import (
    COLORS,
    Logger,
)


@pytest.fixture
def logger():
    return Logger(name="TestLogger", include_name=True)


def test_debug(logger):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.debug("This is a debug message")
        expected_output = f"{COLORS['DEBUG']}DEBUG{COLORS['RESET']} - TestLogger - This is a debug message\n"
        assert mock_stdout.getvalue() == expected_output


def test_info(logger):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.info("This is an info message")
        expected_output = f"{COLORS['INFO']}INFO{COLORS['RESET']} - TestLogger - This is an info message\n"
        assert mock_stdout.getvalue() == expected_output


def test_warning(logger):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.warning("This is a warning message")
        expected_output = f"{COLORS['WARNING']}WARNING{COLORS['RESET']} - TestLogger - This is a warning message\n"
        assert mock_stdout.getvalue() == expected_output


def test_error(logger):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.error("This is an error message")
        expected_output = f"{COLORS['ERROR']}ERROR{COLORS['RESET']} - TestLogger - This is an error message\n"
        assert mock_stdout.getvalue() == expected_output


def test_critical(logger):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.critical("This is a critical message")
        expected_output = f"{COLORS['CRITICAL']}CRITICAL{COLORS['RESET']} - TestLogger - This is a critical message\n"
        assert mock_stdout.getvalue() == expected_output


def test_include_name_false():
    logger = Logger(name="TestLogger", include_name=False)
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.info("This is a test without logger name")
        expected_output = f"{COLORS['INFO']}INFO{COLORS['RESET']} - This is a test without logger name\n"
        assert mock_stdout.getvalue() == expected_output


def test_custom_logger_name():
    logger = Logger(name="CustomLogger", include_name=True)
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        logger.warning("Using a custom logger name")
        expected_output = f"{COLORS['WARNING']}WARNING{COLORS['RESET']} - CustomLogger - Using a custom logger name\n"
        assert mock_stdout.getvalue() == expected_output
