from collections import OrderedDict

from github.Repository import Repository

from pyaction.issues.rendering import IssueTemplate


class IssueForm:
    def __init__(self, repo: Repository, number: int) -> None:
        """initializer

        Args:
            repo (Repository): repository object
            number (int): issue number/ID
        """

        self.issue = repo.get_issue(number)

    def render(self) -> OrderedDict:
        """renders the issue body

        Returns:
            OrderedDict: the issue body in form of dictionary
        """

        template = IssueTemplate(self.issue.body)
        return template.to_dict()
