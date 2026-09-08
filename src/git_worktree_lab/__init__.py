"""用于协作实验的命令行文本工具。"""

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> None:
    """解析命令行参数；基础阶段仅显示帮助。"""
    parser = argparse.ArgumentParser(
        prog="git-worktree-lab",
        description="Git + Worktree 协作实验：命令行文本工具。",
    )
    parser.parse_args(argv)
    parser.print_help()
