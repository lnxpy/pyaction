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
