---
description: Create Github Actions using Python
title: Introduction
---

# Welcome to PyAction! ![Version](https://img.shields.io/pypi/v/pyaction?logo=pypi&logoColor=949DA5&label=Version&labelColor=2A3035&color=4539d0) ![Python Versions](https://img.shields.io/pypi/pyversions/pyaction?logo=python&logoColor=949DA5&label=Python&labelColor=2A3035&color=4539d0)

![header](img/header.svg)

PyAction helps you to create and develop custom GitHub Actions using Python.

> Actions are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, or use and customize actions shared by the GitHub community. ==GitHub Inc.==

This documentation covers a tutorial and a demo hello-world action. Head to [Quickstart](quickstart.md) to see the demo project and create an action in a flash. :zap:

## Easy to Setup
Make sure you have `pip` and `python>=3.8` installed on your machine and install `pyaction`.

```
pip install -U "pyaction[cli]"
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

Here you can see a very basic greeting action example that returns a greeting message to the workflow when someone calls it with a `name` input parameter.

=== ":simple-python: your-action/main.py"

    ```py
    from pyaction import PyAction

    workflow = PyAction()


    @workflow.action()
    def my_action(name: str) -> None:
        workflow.write(
            {
                "phrase": f"Hi {name}!"
            }
        )
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

Since `pyaction` is part of your action's dependencies, you have access to utilities that enable you to work with the repository/workflow data. You can find out more about these utils on the [Tutorial](tutorial.md) page.

## How It Works
Custom GitHub Actions can be developed in different ways. PyAction uses the [Docker Container](https://docs.github.com/en/actions/creating-actions/about-custom-actions#docker-container-actions) method which is highly stable with Python environments. This way, you'll be able to specify the requirements for your actions and run them inside a lightweight isolated container with all the dependencies installed.

If you're interested in the idea and want to help, your contribution is welcome as always. Check out the [Contribution Guide](contributing.md) for more information.
