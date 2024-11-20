import os

from pyaction.workflow import PyAction  # noqa

__version__ = "0.8.1"
__author__ = "Sadra Yahyapour"
__email__ = "lnxpylnxpy@gmail.com"

# package info
PROJECT_NAME = "PyAction"
PACKAGE_NAME = PROJECT_NAME.lower()

# base-url of package
BASE_URL = os.path.dirname(__file__)

# path to the copier template
TEMPLATE_PATH = os.path.join(BASE_URL, "action_template")
