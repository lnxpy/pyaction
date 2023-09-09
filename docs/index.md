---
description: A Cookiecutter template for creating GitHub actions in Python!
---

# Welcome to PyAction Cookiecutter
PyAction is a [Cookiecutter](https://cookiecutter.io) template that allows you to develop GitHub Actions using Python language. This documentation covers a fundamental overview about the project, a demo action, and the key notes you need to remember if you want to push your PyAction actions to the [GitHub Marketplace](https://github.com/marketplace).

```python title="main.py"
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
    main(sys.argv)
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
        name: Using hello-world
        uses: you/your-action@v0.1.0
        with:
          name: John

      - name: Echo message
        run: |
          echo ${{ steps.greetings.outputs.message }}

    ```

## In Theory
Custom GtiHub Actions can be made in the following types.

* Docker-based Actions
* Javascript Actions
* Composite Actions

PyAction is based on the Dockerfile implementation that GitHub recommends and has some workflow-related features that allow you to have access to the variables and data transferring during your workflow run.

## Installation
The first step is to install the `cookiecutter` package on your machine.

```bash
pip install -U cookiecutter
```

To ensure that the installation process was successful, check out the installed version with `-V` flag.

```bash
cookiecutter -V
```

## Usage
Now, it's time for template generation. Easily do this via the following command and after a few promptings, you'll have your very first action generated there.

```
cookiecutter gh:lnxpy/cookiecutter-pyaction
```

In the next section, we'll be taking a look over each question that's being asked and the proper answeres you can give on each one.

### Promting
These are the questions that by answering them, you'll have the most suited action for your case.

??? Failure "Deprecation Alert"
    For the sake of simplicity and faster template generation, I've aimed to remove some of the prompts so that you'll be able to generate your desired action faster with less prompting.

#### `Action name`
The name that you choose from your action.

!!! Warning
    If you're planning to push your action to the GitHub Marketplace, make sure that the _slugged_ version of your action name is unique. To check if it's unique, make sure the following URLs lead you to a _404 page_.

    * https://github.com/marketplace/actions/[slugged-action-name]
    * https://github.com/[slugged-action-name]
    * https://github.com/orgs/[slugged-action-name]

#### `Project slug`
Slugged version of your action name. The best option is to leave it as how it is by default.

#### `Description`
A short description for your action. GitHub will use this description to showcase your action on their [action explore](https://github.com/marketplace/actions/) page.

#### `Author name`
The action author's name. You can put your both first name and last name together.

#### `Email address`
Your email address.

#### `GitHub username or organization`
Your GitHub username or organization.

#### `Starting version`
The beginning version of your action.

#### `Open source license`
Chose an open-source license or `notopensource` if your action is not open-source.

#### `Python version`
The Python version that you want to use in your action. Both Python3.X and Python2.X are supported.

#### `Include dependencies`
Answer `y` if your action has some additional dependencies. This option creates a `requirements.txt` file and adds a new Dockerfile layer before your action execution whereas it ensures that all your dependencies are installed.

```plaintext hl_lines="10"
my-awesome-action
├── Dockerfile
├── LICENSE
├── README.md
├── action.yml
├── actions
│   ├── __init__.py
│   └── io.py
├── main.py
└── requirements.txt
```

!!! Note
    Once you've installed all the dependencies of your action on your machine (or within a `venv`), make sure to run the following command and update the  `requirements.txt` file. Otherwise, your action won't be working properly.

    ```bash
    pip freeze > requirements.txt
    ```

#### `Include badges in readme`
If you want to show <img alt="action-badge" src="https://img.shields.io/badge/Your_Action-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> and <img alt="cookiecutter-pyaction" src="https://img.shields.io/badge/cookiecutter--pyaction-white?logo=cookiecutter&label=Made%20with&labelColor=white&color=0064D7"> badges on your action's README page, then answer `y` to this question.

#### `Branding icon`
Branding icon comes in handy when you want to publish your action in the marketplace. It's basically the icon that's shown as your Action icon. Check out [Feather](https://feathericons.com/) for the available icons that you can use.

#### `Branding color`
Choose a color for your branding icon.

#### `Publish in the marketplace`
This field only shows a warning message about your `Action name` and ensures that you've chosen a unique action name.