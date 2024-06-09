import os
import tempfile

from pyaction.consts import MULTILINE_OUTPUT

test_stream = str(os.path.join(tempfile.gettempdir(), "GITHUB_OUTPUT_TEST.txt"))

test_env_var_context = [
    (
        {"foo": "Foo", "bar": "Bar"},
        "foo=Foo\nbar=Bar\n",
    ),
    (
        {"name": "john", "age": "20", "is_student": "true"},
        "name=john\nage=20\nis_student=true\n",
    ),
]

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
