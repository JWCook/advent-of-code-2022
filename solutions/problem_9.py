#!/usr/bin/env python3
# https://adventofcode.com/2022/day/8
from logging import getLogger

from solutions import INPUTS_DIR

logger = getLogger(__name__)

Coords = tuple[int, int]


def count_moves(data: str) -> int:
    coords_visited = {(0, 0)}
    head_x = head_y = tail_x = tail_y = 0
    # for line in list(data.splitlines())[:20]:
    for line in data.splitlines():
        direction, distance = line[0], int(line[2])
        print(f'[{len(coords_visited):>4}] {direction} {distance}')
        # print(f'{direction} {distance} ({head_x}, {head_y}) ({tail_x}, {tail_y})')
        if direction == 'U':
            for _ in range(distance):
                head_y += 1
                tail_x, tail_y = adjust_tail((head_x, head_y), (tail_x, tail_y))
                coords_visited.add((tail_x, tail_y))
        elif direction == 'D':
            for _ in range(distance):
                head_y -= 1
                tail_x, tail_y = adjust_tail((head_x, head_y), (tail_x, tail_y))
                coords_visited.add((tail_x, tail_y))
        elif direction == 'L':
            for _ in range(distance):
                head_x -= 1
                tail_x, tail_y = adjust_tail((head_x, head_y), (tail_x, tail_y))
                coords_visited.add((tail_x, tail_y))
        elif direction == 'R':
            for _ in range(distance):
                head_x += 1
                tail_x, tail_y = adjust_tail((head_x, head_y), (tail_x, tail_y))
                coords_visited.add((tail_x, tail_y))

    return len(coords_visited)


def adjust_tail(head: Coords, tail: Coords) -> Coords:
    print(f'  ({head[0]}, {head[1]}) ({tail[0]}, {tail[1]})')
    # if is_adjacent(head, tail):
    #     print('    adjacent')
    #     return tail

    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    print(f'    Diff: {x_diff}, {y_diff}')

    if abs(x_diff) > 1:
        adjust = 1 if head[0] > tail[0] else -1
        tail_x = tail[0] + adjust
        print(f'        tail_x: {tail[0]} -> {tail_x}')
        tail = (tail_x, tail[1])
    if abs(y_diff) > 1:
        adjust = 1 if head[1] > tail[1] else -1
        tail_y = tail[1] + adjust
        print(f'        tail_y: {tail[1]} -> {tail_y}')
        tail = (tail[0], tail_y)
    return tail


def is_adjacent(head: Coords, tail: Coords) -> bool:
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_9') as fp:
        data = fp.read()
    logger.info(f'Part 1: {count_moves(data)}')
