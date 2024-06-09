### Action Testing

This directory is a GitHub action that uses the very latest stage of `pyaction` as it [uses `git`](https://github.com/lnxpy/pyaction/blob/ccebecf0b5009772e30526ba296711d01b3e1000/testing_action/requirements.txt#L1) to retrieve the latest change on `pyaction@main` and install it.

It gets triggered when a push happens to `pyaction@main`. This action aims to ensure that the latest commit on PyAction does not break the initial base action structure.
