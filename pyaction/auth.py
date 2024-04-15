import github.Auth
from github import Github


class Auth:
    def __init__(self, token: str) -> None:
        """initializer

        Args:
            token (str): the `GITHUB_TOKEN` value
        """

        self.auth: github.Auth = github.Auth.Token(token)
        self.github: Github = Github(auth=self.auth)
