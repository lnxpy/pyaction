#!/usr/bin/env python
import sys

from coloring import Color, Format, Text

if __name__ == "__main__":
    if "{{ cookiecutter.publish_in_marketplace }}".lower() == "y":
        action_name = "{{ cookiecutter.action_name.lower().replace(' ', '_') }}"

        MARKETPLACE_WARNING = """
        \u26A0\ufe0f  If you want to publish your action in the GitHub marketplace:

            - Make sure {action_name} is unique.
            {footnote}
        """

        print(
            MARKETPLACE_WARNING.format(
                action_name=Text(action_name, options=[Color.YELLOW, Format.BOLD]),
                footnote=Text(
                    "It cannot match an existing action, user, or organization name.",
                    options=[Format.FAINT],
                ),
            ),
        )

        input("Press [ENTER] to continue...")

    sys.exit(0)
