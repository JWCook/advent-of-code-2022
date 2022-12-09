#!/usr/bin/env python3
# https://adventofcode.com/2022/day/8
from logging import getLogger

from solutions import INPUTS_DIR

logger = getLogger(__name__)


class Coord:
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


def count_visited(data: str, n_segments: int = 2) -> int:
    visited = {(0, 0)}
    rope = [Coord() for _ in range(n_segments)]

    for line in data.splitlines():
        direction, distance = line.split()
        logger.debug(f'[{len(visited):>4}] {direction} {distance}')
        for _ in range(int(distance)):
            rope[0].move(direction)
            for i in range(1, n_segments):
                rope[i] = move_segment(rope[i - 1], rope[i])
            visited.add((rope[-1].x, rope[-1].y))

    return len(visited)


def move_segment(head: Coord, tail: Coord) -> Coord:
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


if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_9') as fp:
        data = fp.read()
    logger.info(f'Part 1: {count_visited(data, 2)}')
    logger.info(f'Part 2: {count_visited(data, 10)}')
