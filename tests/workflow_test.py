from pyaction import PyAction


def test_action_decorator(monkeypatch):
    monkeypatch.setenv("INPUT_NAME", "Alice")
    monkeypatch.setenv("INPUT_AGE", "30")
    monkeypatch.setenv("INPUT_IS_STUDENT", "false")

    workflow = PyAction()

    @workflow.action()
    def my_action(name: str, age: int, is_student: bool):
        return (f"{name} is {age} years old", is_student)

    assert my_action == ("Alice is 30 years old", False)
