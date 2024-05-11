from __future__ import annotations

import re


class IssueTemplate:
    def __init__(self, context: str) -> None:
        """initializer

        Args:
            context (str): issue body
        """
        self.context = context

    def to_dict(self) -> dict[str, str]:
        """converting the issue body to dictionary

        Returns:
            Dict[str, str]: issue body in form of dictionary
        """

        pattern = re.compile("### ([^\n]+)\n\n([^#]+)")
        matches = pattern.findall(self.context)

        result = {}
        for match in matches:
            result[match[0].strip()] = match[1].strip()

        return result
