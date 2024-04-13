---
description: Create Github Actions using Python
title: Introduction
---

# Welcome to PyAction!

![header](img/header.svg){ .rounded }

![version)](https://img.shields.io/github/v/tag/lnxpy/pyaction?label=Version&color=4E2DB7) [![Package Testing](https://github.com/lnxpy/pyaction/actions/workflows/testing.yml/badge.svg)](https://github.com/lnxpy/pyaction/actions/workflows/testing.yml) [![docs ci](https://github.com/lnxpy/pyaction/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/lnxpy/pyaction/actions/workflows/docs.yml)

PyAction helps you to create develop custom GitHub Actions using Python.

> Actions are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, or use and customize actions shared by the GitHub community. ==GitHub Inc.==

This documentation covers a tutorial and a demo hello-world action. Head to [Quickstart](quickstart.md) to see the demo project and create an action in a flash. :zap:

## Easy to Setup
Make sure you have `pip` and `python>=3.8` installed on your machine and install `pyaction`.

```
pip install -U pyaction
```

Now, execute the following command to see all the subcommands and options.
```
pyaction --help
```

!!! Example "It's recommended to.."
    Initialize a basic template and provide yourself a nicely put-to-gether action structure for starting.

    ```
    pyaction init
    ```

Here you can see a very basic greeting action example that prints a greeting message when someone calls it with a `name` input parameter.

=== ":simple-python: your-action/main.py"

    ```py
    import sys
    from typing import List

    from pyaction import io


    def main(args: List[str]) -> None:
        """main function

        Args:
            args: STDIN arguments
        """

        name = io.read("name")

        io.write(
            {
              "phrase": f"Hi {name}!"
            }
        )


    if __name__ == "__main__":
        main(sys.argv[1:])

    ```

=== ":simple-github: .github/workflows/ci.yml"

    ```yaml hl_lines="16-18 21"
    name: Greeting Action

    on:
      push:
        branches:
          - main

    jobs:
      build:
        runs-on: ubuntu-latest

        name: Running the action
        steps:
          - name: Greetings
            id: greetings
            uses: you/your-action
            with:
              name: Sadra

          - name: Output
            run: echo ${{ steps.greetings.outputs.phrase }}
    ```

```plaintext title="Output" linenums="1"
▶ Run echo Hi Sadra!
Hi Sadra!
```

Since `pyaction` is part of your action's dependencies, you have access to utilities that enable you to work with the repository/workflow information. You can find out more about these utils on the [Tutorial](tutorial.md) page.

## How It Works
Custom GitHub Actions can be developed in different ways. PyAction uses the [Docker Container](https://docs.github.com/en/actions/creating-actions/about-custom-actions#docker-container-actions) method which is highly stable with Python environments. This way, you'll be able to specify the requirements for your actions and run them inside a lightweight isolated container with all the dependencies installed.

If you're interested in the idea and want to help, your contribution is welcome as always. Check out the [Contribution Guide](contributing.md) for more information.
