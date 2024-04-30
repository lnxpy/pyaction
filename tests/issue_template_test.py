import pytest

from pyaction.issues.rendering import IssueTemplate

test_data = [
    (
        "tests/test_data/issue_template_1.md",
        ["title 1", "title 2", "title 3"],
        ["paragraph 1", "paragraph 2", "paragraph 3"],
    ),
    (
        "tests/test_data/issue_template_2.md",
        ["Text", "Sentences"],
        ["```markdown\nData..\n```", "6"],
    ),
    (
        "tests/test_data/issue_template_3.md",
        [
            "Contact Details",
            "What happened?",
            "Version",
            "What browsers are you seeing the problem on?",
            "Relevant log output",
        ],
        [
            "email address",
            "A bug happened!",
            "1.0.3 (Edge)",
            "Safari, Microsoft Edge",
            "```shell\nsome data\n```",
        ],
    ),
]


@pytest.mark.parametrize("file,titles,values", test_data)
def test_issue_template(file, titles, values):
    with open(file) as md_file:
        context = md_file.read()
        template = IssueTemplate(context).to_dict()

    assert list(template.keys()) == titles
    assert list(template.values()) == values
