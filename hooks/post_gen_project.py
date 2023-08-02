#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

TEMPLATE_CREATION = "\n\r{style}{project_slug}\033[0m is created successfully! \u2705"

FURTHER_INSTRUCTIONS = """
Now you can start working on your action:
    $ cd {project_slug} && git init

Make a commit and upload initial code to GitHub:
    $ git add .
    $ git commit -m "Initial commit"
    $ git tag v{version}
    $ git branch -M main
    $ git remote add origin git@github.com:{github_username}/{project_slug}.git
    $ git push -u origin main --tags"""


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
    # if "{{ cookiecutter.has_dependencies }}".lower() == "n":
    #     remove_file("requirements.txt")

    # if "{{ cookiecutter.open_source_license }}" == "notopensource":
    #     remove_file("LICENSE")

    _files_to_be_removed = [
        "requirements.txt"
        if "{{ cookiecutter.has_dependencies }}".lower() == "n"
        else None,
        "LICENSE"
        if "{{ cookiecutter.open_source_license }}" == "notopensource"
        else None,
    ]

    for path in [_ for _ in _files_to_be_removed if _ is not None]:
        remove_file(path)

    # project created successfully
    print(
        TEMPLATE_CREATION.format(
            project_slug="{{ cookiecutter.project_slug }}", style="\033[1;32m"
        )
    )
    print(
        FURTHER_INSTRUCTIONS.format(
            project_slug="{{ cookiecutter.project_slug }}",
            version="{{ cookiecutter.version }}",
            github_username="{{ cookiecutter.github_username }}",
        )
    )
