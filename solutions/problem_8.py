#!/usr/bin/env python3
# https://adventofcode.com/2022/day/8
from logging import getLogger

from solutions import INPUTS_DIR

logger = getLogger(__name__)


def parse_trees(data: str) -> int:
    tree_grid = [[int(x) for x in line.strip()] for line in data.splitlines()]
    logger.debug(tree_grid)
    grid_height = len(tree_grid)
    grid_width = len(tree_grid[0])

    def is_visible(x, y, tree_grid):
        tree_height = tree_grid[x][y]
        top = [tree_grid[x][i] for i in range(min(y + 1, grid_height), grid_height)]
        bot = [tree_grid[x][i] for i in range(0, y)]
        left = [tree_grid[i][y] for i in range(min(x + 1, grid_width), grid_width)]
        right = [tree_grid[i][y] for i in range(0, x)]
        return any([all([i < tree_height for i in lst]) for lst in [top, bot, left, right]])

    visible_trees = 0
    for x in range(grid_width):
        for y in range(grid_height):
            if is_visible(x, y, tree_grid):
                visible_trees += 1
    return visible_trees


if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_8') as fp:
        data = fp.read()
    logger.info(f'Part 1: {parse_trees(data)}')
