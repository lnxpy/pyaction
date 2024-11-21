import pytest

from pyaction.exceptions import NotAnnotated
from pyaction.workflow.utils import check_parameters

from .test_objects import action_functions

test_annotation_objects = [
    (action_functions.not_annotated, False),
    (action_functions.poorly_annotated, False),
    (action_functions.well_annotated, True),
]


@pytest.mark.parametrize("function,valid", test_annotation_objects)
def test_function_params_annotation(function, valid):
    if not valid:
        with pytest.raises(NotAnnotated):
            check_parameters(function)


valued_test_objects = [
    action_functions.annotated_but_valued_params,
]


@pytest.mark.parametrize("function", valued_test_objects)
def test_function_params_default_values(function, capsys):
    check_parameters(function)
    captured = capsys.readouterr()
    assert "default value" in captured.out
