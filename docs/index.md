---
description: Create Github Actions in Python
title: Introduction
---

![Python Versions](https://img.shields.io/pypi/py_action/copier?color=9002FF)
![PyPI - Version](https://img.shields.io/pypi/v/py_action?color=9002FF)

![banner](img/banner.svg)

**PyAction** is a tool that allows you to develop custom GitHub Actions using Python. This documentation covers the basics and a [Hello-world demo](demo.md) example action.

## Easy to Setup
Make sure you have `pip` and `python>=3.8` installed on your machine and install `py_action`.

```
pip install -U py_action
```

Now, execute the following command to see all the subcommands and options.
```
pyaction --help
```

!!! Example "I highly recommend to.."
    Run `pyaction init` and provide yourself a nicely put-to-gether action template for starting.

Here you can see a very basic hello-world example action generated with `pyaction init`. For a more detailed example, check out the [Hello-world demo](demo.md).

=== ":simple-python: main.py"

    ```py
    import sys
    from typing import List

    from pyaction import io


    def main(args: List[str]) -> None:
        """main function

        Args:
            args: STDIN arguments
        """

        name = io.read("name") #(1)

        io.write(
            {
              "phrase": f"Hi {name}!" #(2)
            }
        )


    if __name__ == "__main__":
        main(sys.argv[1:])

    ```

    1.  This is how we read the input parameters from `with` statement in `.github/workflows/main.yml`:

        ```yaml title=".github/workflows/main.yml" hl_lines="4" linenums="1"
        steps:
          - uses: you/your-action
            with:
              name: Sadra
        ```

    2.  Here is how we return data to the workflow, store it as an environment variable, and use it as input for other steps of the workflow.

        ```yaml title=".github/workflows/main.yml" hl_lines="2 6 10" linenums="1"
        steps:
          - id: greetings
            name: Using your-action
            uses: you/your-action
            with:
              name: Sadra

          - name: Echo message
            run: |
              echo ${{ steps.greetings.outputs.phrase }}
        ```

=== ":simple-yaml: action.yml"

    ```yaml
    name: Greetings Action
    description: This action greets whoever runs it
    author: John Doe

    branding:
      icon: check
      color: blue

    runs:
      using: docker
      image: Dockerfile

    inputs:
      name:
        required: false
        description: the person/thing you want to greet
        default: World

    outputs:
      phrase:
        description: output variable
    ```

```plaintext title="Result"
Hi Sadra!
```

Since `pyaction` is part of your action's dependencies, you have access to utilities that enable you to work with the repository/workflow information.

## How It Works
Custom GitHub Actions can be developed in different ways. PyAction uses the [Docker Container](https://docs.github.com/en/actions/creating-actions/about-custom-actions#docker-container-actions) method which is highly stable with Python environments. This way, you'll be able to specify the requirements for your actions and run them inside a lightweight isolated container with all the dependencies installed.

## Next Steps
I'm planning to expand PyAction's features and availability in other languages. Also trying to keep it up to date with the official changes that GitHub fellows make over on the GitHub Actions infrastructure.

If you're interested in the idea, your contribution is welcome as always. Check out the [Contribution Guide](contributing.md) for more information.
