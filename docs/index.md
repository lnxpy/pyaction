---
description: A Cookiecutter template for creating GitHub actions in Python!
---

# Introducing PyAction
PyAction is a [Cookiecutter](https://cookiecutter.io) template that allows you to develop GitHub Actions using Python language. This documentation covers a fundamental overview of the project, a demo action, and the keynotes you need to remember if you want to push your PyAction actions to the [GitHub Marketplace](https://github.com/marketplace).


```python title="my-awesome-action/main.py"
import os
import sys
from typing import List

from actions import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args (list[str]): STDIN arguments
    """

    name = os.environ["INPUT_NAME"] #(1)

    io.write_to_output(
      {
        "message": f"Hi {name}!" #(2)
      }
    )


if __name__ == "__main__":
    main(sys.argv[1:])
```

1.  Simply read the values that your action users send via the `with` statement within their workflow YAML file.

    ```yaml hl_lines="4" title=".github/workflows/main.yml"
    steps:
      - uses: you/your-action@v0.1.0
        with:
          name: John
    ```

    !!! Warning
        Keep in mind that you have to update the `action.yml` file in order to support receiving the `name` variable from the users respectively.

2.  Here is how you can return data to the workflow, store it, and use it as inputs for other steps inside your workflow. To retrieve `message`, give an `id` to your action execution step and then access the value via `${{ steps.<id>.outputs.message }}`.

    ```yaml hl_lines="2 6 10" title=".github/workflows/main.yml"
    steps:
      - id: greetings
        name: Using your-action
        uses: you/your-action@v0.1.0
        with:
          name: John

      - name: Echo message
        run: |
          echo ${{ steps.greetings.outputs.message }}

    ```

## In Theory
Custom GitHub Actions can be made in the following ways.

* Docker-based Actions
* Javascript Actions
* Composite Actions

PyAction is based on the Dockerfile implementation that GitHub recommends and has some workflow-related features that allow you to have access to the variables and data transferring during your workflow run.

## Installation
The first step is to install the `cookiecutter` package on your machine.

```bash
pip install -U cookiecutter
```

To ensure that the installation process was successful, check out the installed version with the `-V` flag.

```bash
cookiecutter -V
```

## Usage
Now, it's time for template generation. Easily do this via the following command and after a few promptings, you'll have your very first action generated there.

```
cookiecutter gh:lnxpy/cookiecutter-pyaction
```

In the next section, we'll be taking a look over each question that's being asked and the proper answers you can give to each one.

## Promting
These are the questions that by answering them, you'll have the most suited action for your case.

#### `action_name`
The name that you choose from your action.

!!! Warning
    If you're planning to push your action to the GitHub Marketplace, make sure that the _slugged_ version of your action name is unique. To check if it's unique, make sure the following URLs lead you to a _404 page_.

    * https://github.com/marketplace/actions/[slugged-action-name]
    * https://github.com/[slugged-action-name]
    * https://github.com/orgs/[slugged-action-name]

#### `action_slug`
Slugged version of your action name. The best option is to leave it as how it is by default.

#### `description`
A short description of your action. GitHub will use this description to showcase your action on their [action explore](https://github.com/marketplace/actions/) page.

#### `auther_name`
The action author's name. You can put your both first name and last name together.

#### `open_source_license`
Choose an open-source license or `notopensource` if your action is not open-source.

#### `python_version`
The Python version that you want to use in your action. Both Python3.X and Python2.X are supported.

#### `include_dependencies`
Answer `y` if your action has some additional dependencies. This option creates a `requirements.txt` file and adds a new Dockerfile layer before your action execution whereas it ensures that all your dependencies are installed.
