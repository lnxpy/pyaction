from __future__ import annotations

import os

import requests

from pyaction.issues.rendering import IssueTemplate

GITHUB_BASE_URL = "https://api.github.com/"
DEFAULT_TIMEOUT: int = 30  # seconds


class IssueForm:
    def __init__(self, repository: str, number: int, token: str | None = None) -> None:
        """
        Initializer.

        Args:
            repository (str): Repository name in the form of username/repository.
            number (int): Issue number/ID.
            token (Optional[str]): `GITHUB_TOKEN` token. If omitted, the
                `GITHUB_TOKEN` environment variable is used (e.g. in GitHub
                Actions workflows). Defaults to None.
        """
        self._token = token or os.environ.get("GITHUB_TOKEN")
        self.repository = repository
        self.number = number

    def render(self) -> dict[str, str]:
        """
        Renders the issue body.

        Raises:
            requests.HTTPError: If the API request fails (e.g. an invalid
                token or a missing issue).

        Returns:
            Returns the issue body in form of dictionary.
        """
        headers = {"Accept": "application/vnd.github+json"}

        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"

        response = requests.get(
            GITHUB_BASE_URL + f"repos/{self.repository}/issues/{self.number}",
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )
        response.raise_for_status()

        template = IssueTemplate(response.json()["body"])
        return template.to_dict()
