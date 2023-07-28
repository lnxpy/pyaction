#!/usr/bin/env python
import os
import shutil

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
    if "{{ cookiecutter.has_dependencies }}" == "n":
        remove_file("requirements.txt")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
