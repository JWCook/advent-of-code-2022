#!/usr/bin/env python3
# https://adventofcode.com/2022/day/8
from logging import getLogger

from solutions import INPUTS_DIR

logger = getLogger(__name__)
logger.setLevel('DEBUG')


class Coord:
    """pair of coordinates"""

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move(self, direction: str, distance: int = 1) -> None:
        if direction == 'U':
            self.y += distance
        elif direction == 'D':
            self.y -= distance
        elif direction == 'L':
            self.x -= distance
        elif direction == 'R':
            self.x += distance

    def __str__(self) -> str:
        return f'({self.x:>3}, {self.y:>3})'


def count_visited(data: str) -> int:
    visited = {(0, 0)}
    head = Coord()
    tail = Coord()

    # for line in list(data.splitlines())[:20]:
    for line in data.splitlines():
        direction, distance = line.split()
        logger.debug(f'[{len(visited):>4}] {direction} {distance}')
        for _ in range(int(distance)):
            head.move(direction)
            tail = move_tail(head, tail)
            visited.add((tail.x, tail.y))

    return len(visited)


def move_tail(head: Coord, tail: Coord) -> Coord:
    x_diff = abs(head.x - tail.x)
    y_diff = abs(head.y - tail.y)
    logger.debug(f'  {head} {tail} (Diff: {x_diff}, {y_diff})')
    if max(x_diff, y_diff) <= 1:
        return tail

    if x_diff > 0:
        tail.move('R' if head.x > tail.x else 'L')
    if y_diff > 0:
        tail.move('U' if head.y > tail.y else 'D')

    logger.debug(f'  Move:       {tail}')
    return tail


# 2985
# 2975
if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_9') as fp:
        data = fp.read()
    logger.info(f'Part 1: {count_visited(data)}')
