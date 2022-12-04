#!/usr/bin/env python3
# https://adventofcode.com/2022/day/3
from logging import getLogger

from . import INPUTS_DIR

logger = getLogger(__name__)


def char_priority(char: str) -> int:
    """Get character priority using offset from Unicode code point
    Priority: a-z: 1-26, A-Z: 27-52
    """
    offset = 96 if char.islower() else 38
    return ord(char) - offset


def get_str_common_item(line: str) -> str:
    """Get the character that appears in both halves of a string"""
    i = len(line) // 2
    pack_1 = set(line[:i])
    pack_2 = set(line[i:])
    return list(pack_1 & pack_2)[0]


def get_lines_common_item(*lines: str) -> str:
    """Get the character that appears in all specified lines"""
    intersection = set(lines[0])
    for line in lines[1:]:
        intersection &= set(line.strip())
    return list(intersection)[0]


def get_pack_total_priority() -> int:
    total_priority = 0
    with open(INPUTS_DIR / 'input_3') as fp:
        while line := fp.readline():
            common_item = get_str_common_item(line)
            total_priority += char_priority(common_item)
    return total_priority


def get_badge_total_priority() -> int:
    total_priority = 0
    with open(INPUTS_DIR / 'input_3') as fp:
        while True:
            try:
                common_item = get_lines_common_item(next(fp), next(fp), next(fp))
                total_priority += char_priority(common_item)
            except StopIteration:
                break
    return total_priority


def main():
    logger.info(f'Part 1: {get_pack_total_priority()}')
    logger.info(f'Part 2: {get_badge_total_priority()}')


if __name__ == '__main__':
    main()
