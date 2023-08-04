import os


def write_to_output(var: str, val: str) -> None:
    """assigns `val` to `var` in the `GITHUB_OUTPUT` buffer path

    Args:
        var (str): variable name
        val (str): value
    """

    _BUFFER_PATH = os.environ["GITHUB_OUTPUT"]

    with open(_BUFFER_PATH, "a") as _buffer:
        _buffer.write(f"{var}={val}")
