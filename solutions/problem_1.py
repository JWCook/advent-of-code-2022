#!/usr/bin/env python3
# https://adventofcode.com/2022/day/1
from logging import getLogger

from solutions import get_input_data

logger = getLogger(__file__)


def main():
    input = get_input_data(1)
    elf_caloreies = count_calories(input)
    print('Part 1:', elf_caloreies[0])
    print('Part 2:', sum(elf_caloreies[:3]))


def count_calories(input: str) -> list[int]:
    elf_calories = []
    current_elf = 0
    for line in input.splitlines():
        line = line.strip()
        if not line:
            elf_calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    return sorted(elf_calories, reverse=True)


if __name__ == '__main__':
    main()
