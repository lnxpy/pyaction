from unittest.mock import patch

import pytest
from click.testing import CliRunner

from pyaction.cli import cli


@pytest.fixture
def cli_runner():
    """Fixture for Click's CLI runner."""
    return CliRunner()


def test_cli_version(cli_runner):
    """Test the version command."""
    result = cli_runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "PyAction - v" in result.output


@patch("pyaction.cli.run_copy")
def test_cli_init(mock_run_copy, cli_runner):
    """Test the `init` command."""
    result = cli_runner.invoke(cli, ["init"])
    assert result.exit_code == 0
    assert mock_run_copy.called


@patch("os.path.isfile", return_value=True)
@patch("pyaction.cli.load_dotenv")
@patch("subprocess.call")
def test_cli_run_success(mock_subprocess, mock_load_dotenv, mock_isfile, cli_runner):
    """Test the `run` command when `.env` file exists."""
    result = cli_runner.invoke(cli, ["run"])
    assert result.exit_code == 0
    mock_load_dotenv.assert_called_once_with(".env")
    mock_subprocess.assert_called_once_with(["python", "main.py"])
