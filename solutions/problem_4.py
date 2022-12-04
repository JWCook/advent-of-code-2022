#!/usr/bin/env python3
# https://adventofcode.com/2022/day/4
import re
from logging import getLogger
from typing import IO, Iterator

from . import INPUTS_DIR

logger = getLogger(__name__)

IntRanges = tuple[set[int], set[int]]
LINE_PATTERN = re.compile(r'(\d+)\-(\d+),(\d+)-(\d+)')


def parse_ranges(input_fp: IO) -> Iterator[IntRanges]:
    for line in input_fp:
        ints = [int(i) for i in LINE_PATTERN.match(line).groups()]
        yield set(range(ints[0], ints[1] + 1)), set(range(ints[2], ints[3] + 1))


def intersect_ranges(a_start: int, a_end: int, b_start: int, b_end: int) -> set[int]:
    return set(range(a_start, a_end + 1)) & set(range(b_start, b_end + 1))


def has_overlap(range_1: set[int], range_2: set[int]) -> bool:
    """Check if the two ranges have any overlap"""
    return bool(range_1 & range_2)


def is_subset(range_1: set[int], range_2: set[int]) -> bool:
    """Check if either range is a subset of the other"""
    return not range_1 - range_2 or not range_2 - range_1


def count_subsets() -> int:
    n_subsets = 0
    with open(INPUTS_DIR / 'input_4') as fp:
        for range_1, range_2 in parse_ranges(fp):
            if is_subset(range_1, range_2):
                n_subsets += 1
    return n_subsets


def count_overlaps() -> int:
    n_overlaps = 0
    with open(INPUTS_DIR / 'input_4') as fp:
        for range_1, range_2 in parse_ranges(fp):
            if has_overlap(range_1, range_2):
                n_overlaps += 1
    return n_overlaps


def main():
    logger.info(f'Part 1: {count_subsets()}')
    logger.info(f'Part 2: {count_overlaps()}')


if __name__ == '__main__':
    main()
