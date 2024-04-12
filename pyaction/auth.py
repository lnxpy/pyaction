import github.Auth
from github import Github
from github.GithubException import BadCredentialsException

from pyaction.exceptions import BrokenToken


class Auth:
    def __init__(self, token: str) -> None:
        """initializer

        Args:
            token (str): the `GITHUB_TOKEN` value
        """
        self.auth: github.Auth = github.Auth.Token(token)

        self.github: Github = Github(auth=self.auth)
        self.is_authenticated: bool = False

    def authenticate(self) -> None:
        """authenticator

        Raises:
            BrokenToken: if the `token` is broken or not valid
        """
        try:
            _ = self.github.get_user().login
            self.is_authenticated = True
        except BadCredentialsException:
            raise BrokenToken(
                "`GITHUB_TOKEN` value is either not defiend in `action.yml` or not valid."
            )
