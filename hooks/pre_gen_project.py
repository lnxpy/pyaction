import sys

from hooks.utils.messages import MARKETPLACE_WARNING

if __name__ == "__main__":
    if "{{ cookiecutter.publish_in_marketplace }}".lower() == "y":
        print(
            MARKETPLACE_WARNING.format(
                action_name="{{ cookiecutter.action_name.lower().replace(' ', '_') }}"
            )
        )

        input("Press [ENTER] to continue..")

    sys.exit(0)
