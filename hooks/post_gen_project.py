#!/usr/bin/env python
import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"

STARTING_VERSION = "{{ cookiecutter.version }}"

GITHUB_USER = "{{ cookiecutter.github_username }}"

CC_REQUIREMENTS_FILE = "cc_requirements.txt"

GIT_INSTRUCTIONS_INFO = f"""
- Now you can start working on it:

```sh
$ cd {PROJECT_SLUG} && git init
```

- Upload initial code to GitHub:

```sh
$ git add .
$ git commit -m "Initial commit"
$ git tag v{STARTING_VERSION}
$ git branch -M main
$ git remote add origin https://github.com/{GITHUB_USER}/{PROJECT_SLUG}.git
$ git push -u origin main --tags
"""


def remove_file(filepath: str) -> None:
    """removes a file

    Args:
        filepath (str): path to file
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(path: str) -> None:
    """removes a directory recursively

    Args:
        path (str): path to directory
    """
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))


def install_requirements():
    requirements_file = os.path.join(PROJECT_DIRECTORY, CC_REQUIREMENTS_FILE)
    subprocess.check_call(
        [
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-python-version-warning",
            "-qUr",
            requirements_file,
        ]
    )
    remove_file(CC_REQUIREMENTS_FILE)


if __name__ == "__main__":
    if "{{ cookiecutter.has_dependencies }}" == "n":
        remove_file("requirements.txt")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    install_requirements()

    from rich.console import Console
    from rich.markdown import Markdown

    console = Console()

    # project created successfuly
    console.rule(f"[bold white]{PROJECT_SLUG} is created! :fire:")
    console.print(Markdown(GIT_INSTRUCTIONS_INFO))
