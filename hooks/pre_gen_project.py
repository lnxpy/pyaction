#!/usr/bin/env python
import sys

MARKETPLACE_WARNING = """
\u26A0\ufe0f  If you want to publish your action in the GitHub marketplace:

    - make sure {style}{action_name}\033[0m is unique. It cannot match an existing action, user or organization name.
"""

if __name__ == "__main__":
    if "{{ cookiecutter.publish_in_marketplace }}".lower() == "y":
        print(
            MARKETPLACE_WARNING.format(
                action_name="{{ cookiecutter.action_name.lower().replace(' ', '_') }}",
                style="\033[1;32m",
            )
        )

        input("Press [ENTER] to continue..")

    sys.exit(0)
