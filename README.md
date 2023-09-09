## PyAction Cookiecutter [![docs ci](https://github.com/lnxpy/cookiecutter-pyaction/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/lnxpy/cookiecutter-pyaction/actions/workflows/docs.yml) [![main](https://github.com/lnxpy/cookiecutter-pyaction/actions/workflows/main.yml/badge.svg)](https://github.com/lnxpy/cookiecutter-pyaction/actions/workflows/main.yml) ![GitHub tag (with filter)](https://img.shields.io/github/v/tag/lnxpy/cookiecutter-pyaction?label=Version)


`cookiecutter-pyaction` template is a simple Python-supported implementation over the [Docker Container](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action) action type. Follow the steps and make your action in a flash! :zap:

> [!NOTE]
> Read ["Writing GitHub Actions in Python"](https://imsadra.me/writing-github-actions-in-python) article that walks you through a hello-world example.

### Installation
Make sure you have Python and `pip` installed on your machine and install the `cookiecutter` package. That's the template generator tool.

```sh
pip install -U cookiecutter
```

### Usage
In order to create the template, change the directory to the path that you want your action to be in and run the following command.

```sh
cookiecutter gh:lnxpy/cookiecutter-pyaction
```

Keep answering the prompt and your template will be generated.

### Docs
Check out the [official docs](https://pyaction.imsadra.me) for more information about PyAction and a demo hello-world action demonstration.

### Contribution
All your contributions and assistance are welcome. For more information about how you can contribute to the project, please follow the instructions [here](https://pyaction.imsadra.me/contributing). :beers:

### License
Cookiecutter PyAction is licensed under the terms of [MIT License](LICENSE).
