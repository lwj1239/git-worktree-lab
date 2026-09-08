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
