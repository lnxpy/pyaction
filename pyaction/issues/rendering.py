from collections import OrderedDict

import markdown_to_json


class IssueTemplate:
    def __init__(self, context: str) -> None:
        """initializer

        Args:
            context (str): issue body
        """
        self.context = context

    def to_dict(self) -> OrderedDict:
        """convering the issue body to dictionary

        Returns:
            OrderedDict: issue body in form of dictionary
        """

        result = markdown_to_json.dictify(self.context)
        return result
