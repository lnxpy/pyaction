import os
import subprocess

import click
from copier import run_copy
from dotenv import load_dotenv

from pyaction import PROJECT_NAME, TEMPLATE_PATH, __version__


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
    help="Runs the action locally",
)
def run() -> None:
    if not os.path.isfile(".env"):
        raise FileNotFoundError(
            "make sure you have the `.env` file in the root path of your action directory."
        )

    load_dotenv(".env")
    subprocess.call(["python", "main.py"])
