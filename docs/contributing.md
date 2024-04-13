---
title: Contributing
description: Contribution Guide
hide:
  - navigation
---

Thanks for heading over to this page. I assume you're looking for a way to contribute to this project and as always, all your helps are welcome. Follow the instructions and enjoy contributing!

!!! Info "Open an issue first please.."
    I highly recommend you [open an issue](https://github.com/lnxpy/pyaction/issues/new/choose) first. Once we agree on the on-going conversation, then feel free to start working. :beers:

### Fork & Install
Simply fork and clone the repository on your local machine. Change your directory to where the project is. Run the following command to make sure you have `pre-commit` and `tox` installed on your system.

```bash
pip install pre-commit tox && pre-commit install
```

Once you're all set and need to test your changes in the supported environments, simply run `tox` and it'll grab your changes and puts them into test.

If you've changed the docs and want to see the results, run the following command and it'll serve the docs on [localhost:8000](http://localhost:8000).

```bash
tox -e docs
```

??? Note "Access the `venv` that `tox` has created.."
    If you need to access an environment with all the dev dependencies installed, run the following command and it'll create a virtualenv with all the requirements installed in it.

    ```bash
    tox --devenv venv
    source venv/bin/activate
    ```

### Make a Pull Request
If all tests are passed then open a pull-request. :fire:
