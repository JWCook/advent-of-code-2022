#!/usr/bin/env python3
# https://adventofcode.com/2022/day/3
from logging import getLogger
import re
from typing import IO, Iterator

from . import INPUTS_DIR

logger = getLogger(__name__)

LINE_PATTERN = re.compile(r'(\d+)\-(\d+),(\d+)-(\d+)')


def parse_lines(input_fp: IO) -> Iterator[list[int, int, int, int]]:
    for line in input_fp:
        yield [int(i) for i in LINE_PATTERN.match(line).groups()]


def is_subset(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return (a_start <= b_start and a_end >= b_end) or (b_start <= a_start and b_end >= a_end)


def main():
    n_subsets = 0
    with open(INPUTS_DIR / 'input_4') as fp:
        for ranges in parse_lines(fp):
            if is_subset(*ranges):
                n_subsets += 1
    logger.info(f'Part 1: {n_subsets}')


if __name__ == '__main__':
    main()
