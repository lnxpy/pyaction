from pyaction.utils import get_running_platform

TEST_GITHUB_OUTPUT_VALUE = "/github/file_commands/set_output_foo"


def test_get_running_platform_on_runner(monkeypatch):
    monkeypatch.setenv("GITHUB_OUTPUT", TEST_GITHUB_OUTPUT_VALUE)
    assert get_running_platform() == TEST_GITHUB_OUTPUT_VALUE


def test_get_running_platform_on_local():
    assert get_running_platform() is None
