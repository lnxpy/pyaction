<p align="center">
    <img src="assets/logo.svg" width="130">
    <h3 align="center">Cookiecutter PyAction</h3>
    <h6 align="center"><a href="https://github.com/cookiecutter">@cookiecutter</a> template for writing GitHub Actions in Python :package:</h6>
</p><br>

`cookiecutter-pyaction` template is a simple Python-supported implementation over the [Docker Container](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action) action type. Follow the steps and make your action in a flash! :zap:

> [!NOTE]  
> Read ["Writing GitHub Actions in Python"](https://imsadra.me/writing-github-actions-in-python) article which walks you through a hello-world example.

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

#### Publishing in the marketplace
If you want to publish your action in the [GitHub Marketplace](https://github.com/marketplace), make sure to choose a unique name for your action.

#### Action branding
Look [over here](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#brandingicon) for all the available options for the `branding_icon` field.

### Contribution
All your contributions and assistance are welcome. For more information about how you can contribute to the project, please follow the instructions [here](CONTRIBUTING.md). :beers:

### License
Cookiecutter PyAction is licensed under the terms of [MIT License](LICENSE).
