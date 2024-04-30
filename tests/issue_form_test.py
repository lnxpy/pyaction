from unittest.mock import MagicMock

import pytest
from github.Repository import Repository

from pyaction.issues import IssueForm


@pytest.fixture
def mock_repository():
    repo = MagicMock(spec=Repository)
    repo.get_issue.return_value = MagicMock(body="Test issue body")
    return repo


def test_issue_form_render(mock_repository):
    issue_form = IssueForm(mock_repository, 123)
    rendered_issue = issue_form.render()
    assert isinstance(rendered_issue, dict)
