from collections import OrderedDict

import requests

from pyaction.consts import GITHUB_BASE_URL
from pyaction.issues.rendering import IssueTemplate


class IssueForm:
    def __init__(self, repository: str, number: int, token: str = None) -> None:
        """initializer

        Args:
            repository (str): repository name in the form of username/repository
            number (int): issue number/ID
            token (str, optional): GITHUB_TOKEN token. Defaults to None.
        """

        self._token = token
        self.repository = repository
        self.number = number

    def render(self) -> OrderedDict:
        """renders the issue body

        Returns:
            OrderedDict: the issue body in form of dictionary
        """

        headers = {"Accept": "application/vnd.github+json"}

        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"

        issue_payload = requests.get(
            GITHUB_BASE_URL + f"repos/{self.repository}/issues/{self.number}",
            headers=headers,
        ).json()

        template = IssueTemplate(issue_payload["body"])
        return template.to_dict()
