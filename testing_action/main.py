from pyaction import PyAction

workflow = PyAction()


@workflow.action()
def testing_action(test_name: str, test_age: int) -> None:
    workflow.write(
        {
            "message": f"{test_name=} | {test_age=}",
        }
    )
