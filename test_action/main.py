from glorious.pattern import rainbowfier

from pyaction import PyAction
from pyaction.workflow import annotations
from pyaction.workflow.stream import WorkflowContext

workflow = PyAction()


@workflow.action
def testing_action(test_name: str, test_age: int) -> None:
    annotations.warning("This is a warning annotation!")
    annotations.notice("This is a notice annotation!")
    annotations.error("This is an error annotation!")

    workflow.write(
        WorkflowContext(
            {
                "message": rainbowfier(f"{test_name}, you are {test_age}!"),
                "multiline_message": f"{test_name=}\n{test_age=}",
            }
        )
    )
