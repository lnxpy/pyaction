import os
from enum import Enum


# color enum class used by loggers
class Color(Enum):
    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"


# GitHub API service
GITHUB_BASE_URL = "https://api.github.com/"

# package info
PROJECT_NAME = "PyAction"
PACKAGE_NAME = PROJECT_NAME.lower()

# base-url of package
BASE_URL = os.path.dirname(__file__)

# path to the copier template
TEMPLATE_PATH = os.path.join(BASE_URL, "template")

# GITHUB_OUTPUT stream
GITHUB_OUTPUT = os.environ.get("GITHUB_OUTPUT", None)

# Debug mode
DEBUG_MODE = False if GITHUB_OUTPUT else True

# Multi-line format
DELIMITER = "EOF"

MULTILINE_OUTPUT = f"""
{{variable}}<<{DELIMITER}
{{value}}
{DELIMITER}
"""
