import os

# package info
PROJECT_NAME = "PyAction"
PACKAGE_NAME = "pyaction"
PROJECT_DESC = "Create GitHub Actions Using Python"


# Base-url of package
BASE_URL = os.path.dirname(__file__)


# Path to the copier template
TEMPLATE_PATH = os.path.join(BASE_URL, "template")


# GitHub Action's workflow output environment variable
GITHUB_OUTPUT = os.environ.get("GITHUB_OUTPUT", os.devnull)
