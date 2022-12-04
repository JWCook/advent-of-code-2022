#!/usr/bin/env python3
# https://adventofcode.com/2022/day/1
from dataclasses import dataclass
from enum import Enum
from typing import IO, Iterator

from . import INPUTS_DIR


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_char(cls, char: str) -> 'Shape':
        return SHAPE_CODES[char]


SHAPE_CODES = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS,
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS,
}

WIN_CONDITIONS = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER,
}


@dataclass
class Round:
    opponent_shape: Shape
    player_shape: Shape

    @classmethod
    def parse(cls, line: str) -> 'Round':
        opponent_code, player_code = line.strip().split()
        return cls(
            opponent_shape=Shape.from_char(opponent_code),
            player_shape=Shape.from_char(player_code),
        )

    def get_score(self) -> int:
        return self.player_shape.value + self._get_win_score()

    def _get_win_score(self) -> int:
        if self.opponent_shape == self.player_shape:
            return 3
        elif WIN_CONDITIONS[self.player_shape] == self.opponent_shape:
            return 6
        else:
            return 0


def parse_rounds(input_fp: IO):
    while line := input_fp.readline().strip():
        yield Round.parse(line)


def tally_scores() -> int:
    score = 0
    with open(INPUTS_DIR / 'input_2') as f:
        for round in parse_rounds(f):
            score += round.get_score()
    return score


def main():
    print('Part 1:', tally_scores())


if __name__ == '__main__':
    main()
