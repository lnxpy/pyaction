import os
import subprocess

import click
from copier import run_copy

from pyaction import __version__
from pyaction.consts import PROJECT_NAME, TEMPLATE_PATH


@click.version_option(
    __version__,
    prog_name=PROJECT_NAME,
    message="%(prog)s - v%(version)s",
)
@click.group()
def cli():
    """Create GitHub Actions using Python"""
    pass


@cli.command("init", help="Creates a basic action template (recommended for starting)")
def init() -> None:
    run_copy(TEMPLATE_PATH)


@cli.command(
    "run",
    help="Runs the action locally based on the .env file",
)
def run() -> None:
    if not os.path.isfile(".env"):
        raise FileNotFoundError(
            "Make sure you have the `.env` file inside the root path of your action directory."
        )

    subprocess.check_call("env $(cat .env | xargs) python main.py", shell=True)
