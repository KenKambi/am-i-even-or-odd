"""Command-line interface for am-i-even-or-odd.

Usage:
    am-i-even-or-odd 42
    am-i-even-or-odd 42 --fun
"""

import argparse
import random
import sys

from .checker import is_it_even_tho

_EVEN_FUN_LINES = [
    "{n} is even. We checked. Twice. Happy now!?",
  "{n} is even. Forever will be",
  "{n} is even. Obviously...",
  "{n} is even. No plot twists today.",
  "{n} is even. That's low-key satisfying.",
  "{n} is even. As expected. Very demure.",
  "{n} is odd! Kidding it's obviously EVEN.",
  "{n} is even. It's literally divisible by 2. Be serious.",
  "{n} is even Steven",
  "{n} is even. Congratulations, I guess."
]

_ODD_FUN_LINES = [
    "{n} is odd. It really said 'I'm built different.'",
  "{n} is odd. The remainder is literally one.",
  "{n} is odd. We checked. Happy now?",
  "{n} is odd. Not like the other numbers.",
  "{n} is odd. Kinda looks so.",
  "{n} is odd. Bro thinks he's special.",
  "{n} is odd. We all saw this coming.",
  "{n} is even! Kidding it's obviously ODD",
  "{n} is odd. Congratulations, I guess.",
  "{n} is odd. Kinda sus."
]


def _format_result(number: int, even: bool, fun: bool) -> str:
    if not fun:
        return "even" if even else "odd"
    template = random.choice(_EVEN_FUN_LINES if even else _ODD_FUN_LINES)
    return template.format(n=number)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="am-i-even-or-odd",
        description="Find out, once and for all, whether a number is even or odd.",
    )
    parser.add_argument(
        "number",
        type=int,
        help="the whole number to check (e.g. 42, -3, 0)",
    )
    parser.add_argument(
        "--fun",
        action="store_true",
        help="respond with a bit more personality than a plain 'even'/'odd'",
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()

    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        # argparse calls sys.exit() itself on bad input (e.g. "abc" instead
        # of an int); propagate its exit code rather than swallowing it.
        return exc.code if isinstance(exc.code, int) else 2

    even = is_it_even_tho(args.number)
    print(_format_result(args.number, even, args.fun))
    return 0


if __name__ == "__main__":
    sys.exit(main())
