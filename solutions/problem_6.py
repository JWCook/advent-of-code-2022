#!/usr/bin/env python3
# https://adventofcode.com/2022/day/6
from solutions import INPUTS_DIR


def find_marker(message: str, marker_len: int) -> int:
    for i in range(len(message)):
        if len(set(message[i : i + marker_len])) == marker_len:
            return i + marker_len


if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_6') as fp:
        message = fp.read()
    print(f'Part 1: {find_marker(message, 4)}')
    print(f'Part 2: {find_marker(message, 14)}')
