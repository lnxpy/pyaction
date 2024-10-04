## PyAction - Create GitHub Actions Using Python! :sparkles: ![download rate](https://github.com/lnxpy/pyaction/blob/main/.pypi_chart/badge.svg)

![Version)](https://img.shields.io/github/v/tag/lnxpy/pyaction?label=Version) ![Python Versions](https://img.shields.io/pypi/pyversions/pyaction?logo=python&logoColor=949DA5&label=Python&labelColor=2A3035) [![Package Testing](https://github.com/lnxpy/pyaction/actions/workflows/testing.yml/badge.svg)](https://github.com/lnxpy/pyaction/actions/workflows/testing.yml) [![Docs CI](https://github.com/lnxpy/pyaction/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/lnxpy/pyaction/actions/workflows/docs.yml)

PyAction helps you to develop [GitHub Actions](https://docs.github.com/en/actions) using Python. It's delivered as an installable package with the ability to test the action locally before any deployment.

```yml
- name: Using the python action
  uses: you/your-python-action@v2
  with:
      name: Jane
      age: 20
```

```python
from pyaction import PyAction


workflow = PyAction.workflow()

@workflow.action()
def greetings_action(name: str, age: int) -> None:
    workflow.write(
        {
            "phrase": f"Hello {name}. You are {age}!"
        }
    )

# $ pyaction run
# ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Variable ┃          Value          ┃     Type      ┃           Workflow Usage            ┃
# ┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │  phrase  │ Hello Jane. You are 20! │ <class 'str'> │ ${{ steps.STEP_ID.outputs.phrase }} │
# └──────────┴─────────────────────────┴───────────────┴─────────────────────────────────────┘
```

Check out the [official docs](https://pyaction.imsadra.me) for more detailed information. There is also a [Quickstart](https://pyaction.imsadra.me/quickstart) demo tutorial that walks you through a simple hello-world action.

### Installation
Run the following command in a fresh CLI tab.

```sh
pip install -U "pyaction[cli]"
```

To make sure the installation process was successful, run the following command.

```sh
pyaction --version
```

The `pyaction` release is made to be super light which will make your workflow run very fast. The `pyaction[cli]` that you install on your local machine has some additional packages for local development.

### Usage
It's recommended to initialize a template, then going along the development process. Thus, run the `init` command.

```sh
pyaction init
```

Answer the prompts and your template will be generated. Check out the [docs](https://pyaction.imsadra.me) for the further steps.

### Contribution
All your contributions and assistance are welcome. For more information about how you can contribute to the project, please follow the instructions [here](https://pyaction.imsadra.me/contributing). :sparkles:

### License
PyAction is licensed under the [MIT License](LICENSE) terms.
