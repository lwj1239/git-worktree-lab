"""用于协作实验的命令行文本工具。"""

import argparse
from collections.abc import Sequence


def count_words(text: str) -> int:
    """按空白分隔统计单词数量。"""
    return len(text.split())


def main(argv: Sequence[str] | None = None) -> None:
    """解析命令行参数并执行文本处理；无参数时显示帮助。"""
    parser = argparse.ArgumentParser(
        prog="git-worktree-lab",
        description="Git + Worktree 协作实验：命令行文本工具。",
    )
    subparsers = parser.add_subparsers(dest="command")
    count_parser = subparsers.add_parser("count", help="按空白分隔统计单词数量")
    count_parser.add_argument("text", help="待统计的文本")
    upper_parser = subparsers.add_parser("upper", help="将文本转换为大写")
    upper_parser.add_argument("text", help="待转换的文本")

    args = parser.parse_args(argv)
    if args.command == "count":
        print(count_words(args.text))
    elif args.command == "upper":
        print(args.text.upper())
    else:
        parser.print_help()
