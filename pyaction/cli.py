import os
import subprocess

import click
from copier import run_copy

from pyaction import __version__

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "template")


@click.version_option(
    __version__,
    prog_name="PyAction",
    message="%(prog)s ~ version %(version)s",
)
@click.group()
def cli():
    pass


@cli.command("init", help="creates a basic action template (recommended for starting)")
@click.argument("path", default=".")
def init(path: str = ".") -> None:
    run_copy(TEMPLATE_PATH, path)


@cli.command("run", help="uses .env to run the action locally")
def run() -> None:
    try:
        subprocess.check_call(
            "env $(cat .env | xargs) python main.py",
            shell=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        click.echo(
            "Make sure the `.env` file is properly configured based on `action.yml`.",
            err=True,
        )
