#!/usr/bin/env python3
# https://adventofcode.com/2022/day/12
import networkx as nx
from loguru import logger

from solutions import read_input

UNICODE_OFFSET = 96


def parse_map(data: str):
    heightmap = []
    start = None
    end = None
    for y, line in enumerate(data.splitlines()):
        heightmap_row = []
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                height = 1
            elif char == 'E':
                end = (x, y)
                height = 26
            else:
                height = ord(char) - UNICODE_OFFSET
            heightmap_row.append(height)
        heightmap.append(heightmap_row)
    return heightmap, start, end


def format_map(heightmap, path=None):
    return '\n'.join(
        [
            ' '.join(['**' if path and (x, y) in path else f'{i:>2}' for x, i in enumerate(row)])
            for y, row in enumerate(heightmap)
        ]
    )


def build_graph(heightmap: list[list[int]]):
    graph = nx.Graph().to_directed()
    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            graph.add_node((x, y))

    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            for (n_x, n_y) in get_neighbors(heightmap, x, y):
                if (x, y) == (2, 2) and (n_x, n_y) == (3, 2):
                    print('!!!!!!!!!!!!!!')
                    print(x, y, n_x, n_y)
                if (x, y) == (3, 2) and (n_x, n_y) == (2, 2):
                    print('!##!!!!!!!!!!!!!')
                    print(x, y, n_x, n_y)
                graph.add_edge((x, y), (n_x, n_y))
    return graph


def get_neighbors(heightmap: list[list[int]], x: int, y: int):
    neighbors = []
    if x > 0 and (heightmap[y][x - 1] - heightmap[y][x]) <= 1:
        neighbors.append((x - 1, y))
    if x < len(heightmap[0]) - 1 and (heightmap[y][x + 1] - heightmap[y][x]) <= 1:
        neighbors.append((x + 1, y))
    if y > 0 and (heightmap[y - 1][x] - heightmap[y][x]) <= 1:
        neighbors.append((x, y - 1))
    if y < len(heightmap) - 1 and (heightmap[y + 1][x] - heightmap[y][x]) <= 1:
        neighbors.append((x, y + 1))
    return neighbors


def shortest_path(graph, start, end):
    return nx.shortest_path(graph, start, end)


if __name__ == '__main__':
    data = read_input('12')

    heightmap, start, end = parse_map(data)
    logger.info('\n' + format_map(heightmap))
    graph = build_graph(heightmap)
    path = shortest_path(graph, start, end)
    logger.info('\n' + format_map(heightmap, path))
    # print(list(graph.nodes))
    # print(list(graph.edges))
    # print(path)

    logger.info(f'Part 1: \n{len(path)-1}')
