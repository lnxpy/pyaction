---
title: Contributing
description: PyAction contribution guide
---

Thanks for heading over to this index. I assume you're looking for a way to contributing to this project and as always, all your helps are welcome. Follow the instructions in the next sections.

!!! Note "Open an issue first please.."
    I highly recommend you [open an issue](https://github.com/lnxpy/cookiecutter-pyaction/issues/new/choose) first. Once we agree on the theory, then feel free to get your hands dirty. :beers:

### Fork & Install
Simply fork and clone the repository on your local machine. Change your directory to where the project is. Run the following command to make sure you have `pre-commit` and `tox` installed on your system.

```bash
pip install pre-commit tox && pre-commit install
```

Once you're all set and need to test your changes in the supported environments, simply run `tox` and it'll grab your changes and puts them into test.

If you've changed the docs and want to see the resuls, run the following command and it'll serve your docs on `localhost:8000`.

```bash
tox -e docs -- serve
```

??? Note "Access the `venv` that `tox` has created.."
    If you need to access an environment with all the dev dependencies installed, run the following command and it'll create a virtualenv with all the requiremenets installed in it.

    ```bash
    tox --devenv venv
    source venv/bin/activate
    ```

### Make a Pull Request
If all tests are passed then open a pull-request. :fire:
