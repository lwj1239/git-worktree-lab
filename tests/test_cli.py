"""从已安装的命令入口验证用户可见行为。"""

import shutil
import subprocess

import pytest


@pytest.fixture(scope="module")
def command() -> str:
    executable = shutil.which("git-worktree-lab")
    assert executable is not None, "应安装 git-worktree-lab 命令入口"
    return executable


@pytest.mark.parametrize("args", [[], ["--help"], ["-h"]])
def test_help(command: str, args: list[str]) -> None:
    result = subprocess.run(
        [command, *args], capture_output=True, text=True, check=False
    )

    assert result.returncode == 0
    assert "usage: git-worktree-lab" in result.stdout
    assert "-h, --help" in result.stdout
    assert result.stderr == ""


def test_unknown_argument(command: str) -> None:
    result = subprocess.run(
        [command, "--unknown"], capture_output=True, text=True, check=False
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --unknown" in result.stderr
    assert result.stdout == ""


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "2"),
        ("", "0"),
        ("hello  world", "2"),
        ("hello\tworld", "2"),
        ("hello\nworld", "2"),
        (" \t\n ", "0"),
        ("  hello \t world\nagain  ", "3"),
    ],
    ids=["basic", "empty", "repeated-space", "tab", "newline", "whitespace-only", "mixed"],
)
def test_count(command: str, text: str, expected: str) -> None:
    result = subprocess.run(
        [command, "count", text], capture_output=True, text=True, check=False
    )

    assert result.returncode == 0
    assert result.stdout == expected + "\n"
    assert result.stderr == ""


def test_count_requires_text(command: str) -> None:
    result = subprocess.run(
        [command, "count"], capture_output=True, text=True, check=False
    )

    assert result.returncode == 2
    assert "the following arguments are required: text" in result.stderr
    assert result.stdout == ""
