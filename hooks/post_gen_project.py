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
    REMOVE_PATHS = [
        "{% if cookiecutter.include_dependencies.lower() == 'n' %} requirements.txt {% endif %}",
        "{% if cookiecutter.open_source_license == 'notopensource' %} LICENSE {% endif %}",
    ]

    for path in REMOVE_PATHS:
        if path:
            remove_file(path.strip())

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
