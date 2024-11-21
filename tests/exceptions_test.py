import pytest

from pyaction.exceptions import (
    NotAnnotated,
    WorkflowParameterNotFound,
)


def test_workflow_parameter_not_found_exception():
    with pytest.raises(WorkflowParameterNotFound) as exc_info:
        raise WorkflowParameterNotFound("Parameter 'x' is missing from the workflow")
    assert str(exc_info.value) == "Parameter 'x' is missing from the workflow"
    assert isinstance(exc_info.value, WorkflowParameterNotFound)


def test_not_annotated_exception():
    with pytest.raises(NotAnnotated) as exc_info:
        raise NotAnnotated("The function 'example_function' is not properly annotated")
    assert (
        str(exc_info.value)
        == "The function 'example_function' is not properly annotated"
    )
    assert isinstance(exc_info.value, NotAnnotated)
