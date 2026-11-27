from unittest.mock import patch

import pytest

from pyaction.workflow.annotations import error, notice, warning


@pytest.fixture
def mock_subprocess_call():
    """Fixture for mocking subprocess.call."""
    with patch("subprocess.call") as mock_call:
        yield mock_call


@pytest.fixture
def mock_get_running_platform():
    """Fixture for mocking get_running_platform."""
    with patch("pyaction.utils.get_running_platform") as mock_platform:
        yield mock_platform


def test_error_on_runner(mock_subprocess_call, mock_get_running_platform):
    """Test error function when running on a runner."""
    mock_get_running_platform.return_value = True  # Simulates being on a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        error("Test Error")
        mock_subprocess_call.assert_called_once_with(["echo", "::error::Test Error"])


def test_error_off_runner(mock_subprocess_call, mock_get_running_platform):
    """Test error function when not running on a runner."""
    mock_get_running_platform.return_value = False  # Simulates being off a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", False):
        error("Test Error")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "Error Annotation: Test Error"]
        )


def test_warning_on_runner(mock_subprocess_call, mock_get_running_platform):
    """Test warning function when running on a runner."""
    mock_get_running_platform.return_value = True  # Simulates being on a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        warning("Test Warning")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "::warning::Test Warning"]
        )


def test_warning_off_runner(mock_subprocess_call, mock_get_running_platform):
    """Test warning function when not running on a runner."""
    mock_get_running_platform.return_value = False  # Simulates being off a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", False):
        warning("Test Warning")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "Warning Annotation: Test Warning"]
        )


def test_notice_on_runner(mock_subprocess_call, mock_get_running_platform):
    """Test notice function when running on a runner."""
    mock_get_running_platform.return_value = True  # Simulates being on a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        notice("Test Notice")
        mock_subprocess_call.assert_called_once_with(["echo", "::notice::Test Notice"])


def test_notice_off_runner(mock_subprocess_call, mock_get_running_platform):
    """Test notice function when not running on a runner."""
    mock_get_running_platform.return_value = False  # Simulates being off a runner
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", False):
        notice("Test Notice")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "Notice Annotation: Test Notice"]
        )


def test_notice_with_full_metadata_on_runner(
    mock_subprocess_call, mock_get_running_platform
):
    """Test notice function with all metadata properties on a runner."""
    mock_get_running_platform.return_value = True
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        notice(
            "Test Notice",
            title="Heads Up",
            file="app.py",
            line=3,
            end_line=5,
            col=7,
            end_column=9,
        )
        mock_subprocess_call.assert_called_once_with(
            [
                "echo",
                "::notice title=Heads Up,file=app.py,line=3,endLine=5,col=7,endColumn=9::Test Notice",
            ]
        )


def test_error_with_partial_metadata_on_runner(
    mock_subprocess_call, mock_get_running_platform
):
    """Test error function with some metadata properties on a runner."""
    mock_get_running_platform.return_value = True
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        error("Deployment Failed", title="Deploy Check", file="main.py")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "::error title=Deploy Check,file=main.py::Deployment Failed"]
        )


def test_metadata_escaping_on_runner(mock_subprocess_call, mock_get_running_platform):
    """Test that metadata properties and messages are properly escaped."""
    mock_get_running_platform.return_value = True
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", True):
        warning("Progress 50%:\ndone", title="a,b:c", file="my,file.py")
        mock_subprocess_call.assert_called_once_with(
            [
                "echo",
                "::warning title=a%2Cb%3Ac,file=my%2Cfile.py::Progress 50%25:%0Adone",
            ]
        )


def test_notice_with_metadata_off_runner(
    mock_subprocess_call, mock_get_running_platform
):
    """Test that metadata is ignored when not running on a runner."""
    mock_get_running_platform.return_value = False
    with patch("pyaction.workflow.annotations.RUNNING_ON_RUNNER", False):
        notice("Test Notice", title="Heads Up")
        mock_subprocess_call.assert_called_once_with(
            ["echo", "Notice Annotation: Test Notice"]
        )
