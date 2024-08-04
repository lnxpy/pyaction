from unittest.mock import patch

from pyaction.issues import IssueForm
from pyaction.issues.rendering import IssueTemplate


@patch("requests.get")
def test_render_with_token(mock_requests_get):
    issue_body = {"body": "Mock issue body for testing"}
    mock_requests_get.return_value.json.return_value = issue_body

    issue_form = IssueForm("testuser/testrepo", 123, "SOMETOKEN")
    rendered_issue = issue_form.render()

    assert isinstance(rendered_issue, dict)
    assert rendered_issue == IssueTemplate(issue_body["body"]).to_dict()


@patch("requests.get")
def test_render_without_token(mock_requests_get):
    issue_body = {"body": "Mock issue body for testing"}
    mock_requests_get.return_value.json.return_value = issue_body

    issue_form = IssueForm("testuser/testrepo", 123)
    rendered_issue = issue_form.render()

    assert isinstance(rendered_issue, dict)
    assert rendered_issue == IssueTemplate(issue_body["body"]).to_dict()
