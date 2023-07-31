#!/usr/bin/env python
import os
import shutil

from hooks.messages import FURTHER_INSTRUCTIONS, TEMPLATE_CREATION

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


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


if __name__ == "__main__":
    if "{{ cookiecutter.has_dependencies }}".lower() == "n":
        remove_file("requirements.txt")

    if "{{ cookiecutter.open_source_license }}" == "notopensource":
        remove_file("LICENSE")

    # project created successfully
    print(TEMPLATE_CREATION.format(project_slug="{{ cookiecutter.project_slug }}"))
    print(
        FURTHER_INSTRUCTIONS.format(
            project_slug="{{ cookiecutter.project_slug }}",
            version="{{ cookiecutter.version }}",
            github_username="{{ cookiecutter.github_username }}",
        )
    )
