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
