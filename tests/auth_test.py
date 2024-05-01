import github

from pyaction.auth import Auth


def test_auth_object():
    token = "SOME-TOKEN"
    instance = Auth(token)

    assert isinstance(instance.github, github.Github)
    assert isinstance(instance.auth, github.Auth.Auth)
