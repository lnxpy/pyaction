import os
import sys
import tempfile

import pytest
from rich.console import Console

from pyaction import io
from pyaction.consts import MULTILINE_OUTPUT
from pyaction.exceptions import WorkflowParameterNotFound
from pyaction.utils import create_output_table

test_env_vars = [
    ("INPUT_FOO", "foo", "Alice"),
    ("INPUT_BAR", "bar", "20"),
    ("INPUT_BAZ", "baz", "true"),
    ("INPUT_QUX", "qux", "2020.05.03"),
]

test_stream = str(os.path.join(tempfile.tempdir, "GITHUB_OUTPUT_TEST.txt"))


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
    io.write(context, test_stream)

    with open(test_stream, "r+") as file:
        content = file.read()

    assert content == expected


test_multi_line_env_var_context = [
    (
        {"message": "Hello\nworld"},
        MULTILINE_OUTPUT.format(variable="message", value="Hello\nworld"),
    ),
    (
        {"phrase": "How\nAre\nYou?!"},
        MULTILINE_OUTPUT.format(variable="phrase", value="How\nAre\nYou?!"),
    ),
]


@pytest.mark.parametrize("context,expected", test_multi_line_env_var_context)
def test_write_multiline_to_stream(context, expected):
    io.write(context, test_stream)

    with open(test_stream, "r+") as file:
        content = file.read()

    assert content == expected


test_stdout_env_var_context = [
    (
        {"name": "Alex"},
        ["name", "Alex", str(str), "${{ steps.STEP_ID.outputs.name }}"],
    ),
    (
        {"name": "Joe"},
        ["name", "Joe", str(str), "${{ steps.STEP_ID.outputs.name }}"],
    ),
]


@pytest.mark.parametrize("vars,cells", test_stdout_env_var_context)
def test_write_to_stdout(capsys, vars, cells):
    table = create_output_table()
    console = Console()

    table.add_row(*cells)

    io.write(vars, stream=sys.stdout)
    result_capture = capsys.readouterr()

    console.print(table)
    expected_capture = capsys.readouterr()

    assert result_capture.out == expected_capture.out
