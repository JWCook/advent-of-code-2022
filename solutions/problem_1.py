#!/usr/bin/env python3
# https://adventofcode.com/2022/day/1
from logging import getLogger
from typing import IO, Iterator

from . import INPUTS_DIR

logger = getLogger(__name__)


def get_elf_calories(input_fp: IO) -> Iterator[int]:
    def next_elf_calories():
        calories = 0
        while line := next(input_fp).strip():
            calories += int(line)
        return calories

    while True:
        try:
            yield next_elf_calories()
        # next() raises StopIteration when it reaches EOF
        except StopIteration:
            break


def main():
    with open(INPUTS_DIR / 'input_1') as fp:
        elf_calories = sorted(get_elf_calories(fp), reverse=True)
    logger.info(f'Part 1: {elf_calories[0]}')
    logger.info(f'Part 2: {sum(elf_calories[:3])}')


if __name__ == '__main__':
    main()
