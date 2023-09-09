#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
TEMPLATE_CREATION_MESSAGE = (
    "{style}{action_slug}\033[0m is created successfully! \u2705"
)


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
    REMOVE_PATHS = [
        "{% if cookiecutter.include_dependencies.lower() == 'n' %} requirements.txt {% endif %}",
        "{% if cookiecutter.open_source_license == 'notopensource' %} LICENSE {% endif %}",
    ]

    for path in REMOVE_PATHS:
        if path:
            remove_file(path.strip())

    # project created successfully
    print(
        TEMPLATE_CREATION_MESSAGE.format(
            action_slug="{{ cookiecutter.action_slug }}", style="\033[1;32m"
        )
    )
