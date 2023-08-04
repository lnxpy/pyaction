## Contribution Guide
Thanks for heading over to this index. I assume you're looking for a way to contributing to this repository and as always, all your helps are welcome. Follow the instructions in the next sections.

> I highly recommend you to open an issue first. Once we achieve an agreement over the changes, feel free to get your hands dirty then. :beers:

### Fork & Install
Simply fork and clone the repository on your local machine. Change your directory to where the project is. Run the following command to make sure you have `pre-commit` and `tox` installed on your system. (you can do it in a `virtualenv` as well)

```sh
pip install pre-commit tox && pre-commit install
```

Once you're all set and need to test your changes in the supported environments, simply run `tox` and it'll grab your changes and put them into tests.

### Make a Pull Request
If all tests are passed and you think there are no linting and formatting issues with your changes, feel free to open a pull-request.
