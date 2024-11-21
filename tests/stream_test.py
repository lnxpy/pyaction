import json
import os
import tempfile

import pytest

from pyaction.workflow.stream import (
    MULTILINE_OUTPUT,
    push_to_local,
    push_to_runner,
)

tmp_stream = str(os.path.join(tempfile.gettempdir(), "GITHUB_OUTPUT_TEST.txt"))

test_context = [
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


@pytest.mark.parametrize("context,value", test_context)
def test_push_to_runner_stream(context, value):
    _ = push_to_runner(context, tmp_stream)

    with open(tmp_stream) as file:
        assert file.read() == value


@pytest.mark.parametrize("context,value", test_context)
def test_local_stream(capsys, context, value):
    expected_output = []
    for var, val in context.items():
        expected_output.append(
            {
                "var": var,
                "value": val,
                "type": str(type(val)),
                "usage": f"${{{{ steps.STEP_ID.outputs.{var} }}}}",
            }
        )

    push_to_local(context)
    captured = json.loads(capsys.readouterr().out)
    assert captured == expected_output
