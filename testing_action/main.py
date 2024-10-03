from glorious.pattern import rainbowify

from pyaction import PyAction

workflow = PyAction()


@workflow.action()
def testing_action(test_name: str, test_age: int) -> None:
    workflow.warning("This is a warning annotation!")
    workflow.notice("This is a notice annotation!")
    workflow.error("This is an error annotation!")

    workflow.write(
        {
            "message": rainbowify(f"{test_name}, you are {test_age}!"),
            "multiline_message": f"{test_name=}\n{test_age=}",
        }
    )
