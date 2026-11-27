from unittest.mock import MagicMock, patch

import pytest
import requests

from pyaction.issues.connector import IssueForm

ISSUE_BODY = "### Name\n\nJohn\n\n### Age\n\n20"


def _mock_response(status_code: int = 200, body: str = ISSUE_BODY) -> MagicMock:
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = {"body": body}
    if status_code >= 400:
        response.raise_for_status.side_effect = requests.HTTPError(
            f"{status_code} error"
        )
    return response


@patch("pyaction.issues.connector.requests.get")
def test_render_parses_the_issue_body(mock_get):
    mock_get.return_value = _mock_response()

    result = IssueForm("user/repo", 1, token="t").render()

    assert result == {"Name": "John", "Age": "20"}


@patch("pyaction.issues.connector.requests.get")
def test_token_is_sent_as_bearer_header(mock_get):
    mock_get.return_value = _mock_response()

    IssueForm("user/repo", 1, token="t").render()

    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"] == "Bearer t"


@patch("pyaction.issues.connector.requests.get")
def test_no_token_means_no_auth_header(mock_get):
    mock_get.return_value = _mock_response()

    IssueForm("user/repo", 1).render()

    headers = mock_get.call_args.kwargs["headers"]
    assert "Authorization" not in headers


@patch("pyaction.issues.connector.requests.get")
def test_github_token_env_fallback(mock_get, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "env-token")
    mock_get.return_value = _mock_response()

    IssueForm("user/repo", 1).render()

    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"] == "Bearer env-token"


@patch("pyaction.issues.connector.requests.get")
def test_http_errors_are_raised(mock_get):
    mock_get.return_value = _mock_response(status_code=404)

    with pytest.raises(requests.HTTPError):
        IssueForm("user/repo", 1, token="t").render()


@patch("pyaction.issues.connector.requests.get")
def test_request_has_a_timeout(mock_get):
    mock_get.return_value = _mock_response()

    IssueForm("user/repo", 1, token="t").render()

    assert mock_get.call_args.kwargs["timeout"] == 30
