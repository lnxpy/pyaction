## PyAction - Create GitHub Actions Using Python! :sparkles: ![download rate](https://github.com/lnxpy/pyaction/blob/main/.pypi_chart/badge.svg)

[![pyaction](https://img.shields.io/badge/PyAction-black?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDAgNjAwIj4KICA8ZGVmcz4KICAgIDxzdHlsZT4KICAgICAgLmNscy0xIHsKICAgICAgICBmaWxsOiAjZmZmOwogICAgICAgIGZpbGwtcnVsZTogZXZlbm9kZDsKICAgICAgfQogICAgPC9zdHlsZT4KICA8L2RlZnM+CiAgPGcgaWQ9IlNWR1JlcG9faWNvbkNhcnJpZXIiIGRhdGEtbmFtZT0iU1ZHUmVwbyBpY29uQ2FycmllciI+CiAgICA8cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0zNjAuNywyMjAuNDNsMjMzLjUzLDI1Mi4zMkwzMzEuNTksMTguODksNS45Niw1ODEuM0gzNzUuMmwtMjI0LjMxLTY1LjUzYy0xMi42MS0zLjY5LTE3Ljc5LTE4Ljc0LTEwLjA3LTI5LjRMMzMxLjM5LDIyMi4xOGM2Ljk4LTkuNzIsMjEuMTgtMTAuNTcsMjkuMy0xLjc0WiIvPgogIDwvZz4KPC9zdmc+)](https://pyaction.imsadra.me/) ![version](https://img.shields.io/github/v/tag/lnxpy/pyaction?style=for-the-badge&label=version&labelColor=black&color=white)
 ![python versions](https://img.shields.io/pypi/pyversions/pyaction?logo=python&logoColor=white&label=Python&labelColor=black&style=for-the-badge&color=white) [![testing status](https://img.shields.io/github/actions/workflow/status/lnxpy/pyaction/testing.yml?branch=main&style=for-the-badge&label=test&labelColor=black&color=white)
](https://github.com/lnxpy/pyaction/actions/workflows/testing.yml)

PyAction helps you to develop [GitHub Actions](https://docs.github.com/en/actions) using Python. It's delivered as an installable package with the ability to run and test the action locally before any deployment.

```yml
- name: Using the python action
  uses: you/your-python-action@v2
  with:
      name: Jane
      age: 20
```

```python
from pyaction import PyAction


workflow = PyAction()

@workflow.action
def greetings_action(name: str, age: int) -> None:
    workflow.write(
        {
            "phrase": f"Hello {name}. You are {age}!"
        }
    )

# $ pyaction run
# [
#    {
#       "var": "phrase",
#       "value": "Hello Jane. You are 20!",
#       "type": "<class 'str'>",
#       "usage": "${{ steps.STEP_ID.outputs.phrase }}"
#    }
# ]
```

Check out the [official docs](https://pyaction.imsadra.me/docs) for more detailed information. There is also a [Quickstart](https://pyaction.imsadra.me/docs/overview/quickstart) demo tutorial that walks you through a simple hello-world action.

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

Answer the prompts and your template will be generated. Check out the [docs](https://pyaction.imsadra.me/docs) for the further steps.

### Contribution
All your contributions and assistance are welcome. For more information about how you can contribute to the project, please follow the instructions [here](https://pyaction.imsadra.me/docs/more/contributing). :sparkles:

### License
PyAction is licensed under the [MIT License](LICENSE) terms.
