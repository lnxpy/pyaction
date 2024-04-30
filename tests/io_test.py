import os
import tempfile

import pytest

from pyaction import io
from pyaction.exceptions import WorkflowParameterNotFound

test_env_vars = [
    ("INPUT_FOO", "foo", "Alice"),
    ("INPUT_BAR", "bar", "20"),
    ("INPUT_BAZ", "baz", "true"),
    ("INPUT_QUX", "qux", "2020.05.03"),
]


@pytest.mark.parametrize("var,name,val", test_env_vars)
def test_io_read(monkeypatch, var, name, val):
    monkeypatch.setenv(var, val)
    assert io.read(name) == val


def test_io_read_missing_parameters():
    with pytest.raises(WorkflowParameterNotFound):
        io.read("name")


test_env_var_context = [
    ({"foo": "Foo", "bar": "Bar"}, "foo=Foo\nbar=Bar\n"),
    (
        {"name": "john", "age": "20", "is_student": "true"},
        "name=john\nage=20\nis_student=true\n",
    ),
]


@pytest.mark.parametrize("context,expected", test_env_var_context)
def test_write_to_stream(context, expected):
    test_stream = os.path.join(tempfile.tempdir, "GITHUB_OUTPUT_TEST.txt")
    io.write(context, str(test_stream))

    with open(test_stream, "r+") as file:
        content = file.read()

    assert content == expected
