import pytest

from pyaction.utils import check_parameters
from pyaction.exceptions import NotAnnotated

from .test_objects import action_functions


annotation_test_objects = [
    (action_functions.not_annotated, False),
    (action_functions.poorly_annotated, False),
    (action_functions.well_annotated, True),
]


@pytest.mark.parametrize("function,valid", annotation_test_objects)
def test_function_params_annotation(function, valid):
    if not valid:
        with pytest.raises(NotAnnotated):
            check_parameters(function)


valued_test_objects = [
    action_functions.annotated_but_valued_params,
]


@pytest.mark.parametrize("function", valued_test_objects)
def test_function_params_default_values(function, caplog):
    check_parameters(function)
    assert "default value" in caplog.text
