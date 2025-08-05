#!/usr/bin/env python3

import argparse
import textwrap
from pathlib import Path


def main(args):
    print(args)


def parse_args():
    arg_parser = argparse.ArgumentParser(
        allow_abbrev=True,
        description=textwrap.dedent(
            """Find a consensus text sequence given several versions of it."""
        ),
    )

    arg_parser.add_argument(
        "--annotations",
        type=Path,
        metavar="PATH",
        help="""Annotations JSON file.""",
    )

    args = arg_parser.parse_args()
    return args


if __name__ == "__main__":
    ARGS = parse_args()
    main(ARGS)
