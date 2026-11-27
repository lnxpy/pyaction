from __future__ import annotations

import os


def get_running_platform() -> str | None:
    """
    Determine the current operating environment for the action.

    Returns:
        Returns the value stored in the `GITHUB_OUTPUT` environment variable if the action is running on Runner; otherwise, returns `None`.
    """
    return os.environ.get("GITHUB_OUTPUT", None)
