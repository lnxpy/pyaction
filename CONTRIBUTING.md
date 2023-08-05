## Contribution Guide
Thanks for heading over to this index. I assume you're looking for a way to contributing to this repository and as always, all your helps are welcome. Follow the instructions in the next sections.

> I highly recommend you open an issue first. Once we agree on the theory, then feel free to get your hands dirty. :beers:

### Fork & Install
Simply fork and clone the repository on your local machine. Change your directory to where the project is. Run the following command to make sure you have `pre-commit` and `tox` installed on your system.

```sh
pip install pre-commit tox && pre-commit install
```

Once you're all set and need to test your changes in the supported environments, simply run `tox` and it'll grab your changes and put them into tests.

If you need to access an environment with all the dev dependencies installed, run the following command and it'll create a virtualenv with all the requiremenets installed in it.

```
tox --devenv venv
source venv/bin/activate
```

### Make a Pull Request
If all tests are passed then open a pull-request. :fire:
