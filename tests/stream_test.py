import os
import tempfile

import pytest
from rich.console import Console

from pyaction.consts import MULTILINE_OUTPUT
from pyaction.workflow.stream import LocalStream, WorkflowStream
from pyaction.workflow.utils import generate_param_table

tmp_stream = str(os.path.join(tempfile.gettempdir(), "GITHUB_OUTPUT_TEST.txt"))

test_env_var_context = [
    (
        {"foo": "Bar", "baz": "Buff"},
        "foo=Bar\nbaz=Buff\n",
    ),
    (
        {"name": "john", "age": "20", "is_student": "true"},
        "name=john\nage=20\nis_student=true\n",
    ),
    (
        {"message": "Hello\nworld"},
        MULTILINE_OUTPUT.format(variable="message", value="Hello\nworld"),
    ),
    (
        {"phrase": "How\nAre\nYou?!"},
        MULTILINE_OUTPUT.format(variable="phrase", value="How\nAre\nYou?!"),
    ),
]


@pytest.mark.parametrize("context,expected", test_env_var_context)
def test_workflow_stream(context, expected):
    stream = WorkflowStream(stream=tmp_stream)
    stream.put(context)

    with open(tmp_stream) as file:
        assert file.read() == expected


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


@pytest.mark.parametrize("context,row", test_stdout_env_var_context)
def test_local_stream(capsys, context, row):
    stream = LocalStream()
    console = Console()

    stream.put(context)
    captured_table = capsys.readouterr()

    table = generate_param_table()
    table.add_row(*row)

    console.print(table)
    expected_table = capsys.readouterr()

    assert captured_table == expected_table
