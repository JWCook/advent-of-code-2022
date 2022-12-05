#!/usr/bin/env python3
# https://adventofcode.com/2022/day/5
import re
from collections import deque
from logging import getLogger

from . import INPUTS_DIR

logger = getLogger(__name__)

MOVE_PATTERN = re.compile('move (\d+) from (\d+) to (\d+)')

"""
[T]     [Q]             [S]
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
"""


def process_crates(lines: list[str], multicrate_moves: bool = False) -> str:
    lines = iter(lines)

    # Parse crate text into stacks (bottom crates first)
    crate_rows = []
    while '[' in (line := next(lines)):
        crate_rows.append(parse_crate_line(line))
    stacks = [get_stack(crate_rows, col) for col in range(len(crate_rows[0]))]
    logger.debug(_str_stacks(stacks))

    # Process crate moves
    while line := next(lines, None):
        match = MOVE_PATTERN.match(line)
        if not match:
            continue
        count, src, dest = [int(i) for i in match.groups()]
        logger.debug(f'Moving {count} crates from {src} to {dest}')
        moved_crates = [stacks[src - 1].pop() for _ in range(count)]
        if multicrate_moves:
            moved_crates.reverse()
        stacks[dest - 1].extend(moved_crates)

    logger.debug(_str_stacks(stacks))
    return ''.join([stack.pop() for stack in stacks])


def parse_crate_line(line: str) -> list[str]:
    """Parse a row of 'crates' into a list; 0 = empty"""
    line = line.replace('    ', ' [0]').replace('\n', '')
    line = re.sub(r'[ \[\]]', '', line)
    return list(line)


def get_stack(crate_rows: list[list[str]], col: int) -> deque[str]:
    return deque([row[col] for row in reversed(crate_rows) if row[col] != '0'])


def _str_stacks(stacks):
    stack_strs = [' '.join([f'[{c}]' for c in stack]) for stack in stacks]
    return '\n' + '\n'.join(stack_strs)


def main():
    with open(INPUTS_DIR / 'input_5') as fp:
        lines = fp.readlines()
    logger.info(f'Part 1: {process_crates(lines)}')
    logger.info(f'Part 2: {process_crates(lines, multicrate_moves=True)}')


if __name__ == '__main__':
    main()
