#!/usr/bin/env python3
# https://adventofcode.com/2022/day/11
import re
from dataclasses import dataclass, field
from typing import Callable, Iterator

from loguru import logger

from solutions import read_input

MONKEY_PATTERN = re.compile(
    r'(\d+):\n\s+Starting items: (.+)\n\s*'
    r'Operation: new = (.*)\n\s*'
    r'Test: divisible by (.+)\n\s*'
    r'If true: throw to monkey (\d+)\n\s*'
    r'If false: throw to monkey (\d+)',
    re.MULTILINE,
)


@dataclass
class Monkey:
    id: int = field()
    items: list[int] = field()
    operation: Callable = field()
    test_divisible: int = field()
    next_true: int = field()
    next_false: int = field()
    n_inspected: int = field(default=0)

    @classmethod
    def parse(cls, monkey_str: str) -> 'Monkey':
        tokens = MONKEY_PATTERN.match(monkey_str).groups()

        def operation(x: int):
            operation_str = tokens[2].replace('old', str(x))
            print(f'Op: {operation_str} | {x} | {eval(operation_str)}')
            return eval(operation_str)

        return cls(
            id=int(tokens[0]),
            items=[int(item.strip()) for item in tokens[1].split(',')],
            operation=operation,
            test_divisible=int(tokens[3]),
            next_true=int(tokens[4]),
            next_false=int(tokens[5]),
        )

    @property
    def items_str(self) -> str:
        return ", ".join([str(i) for i in self.items])

    def inspect_items(self) -> Iterator[tuple[int, int]]:
        for item in self.items:
            yield self.next_monkey(item)
            self.n_inspected += 1
        self.items = []

    def next_monkey(self, item: int) -> tuple[int, int]:
        item = int(self.operation(item) / 3)
        passed_test = item % self.test_divisible == 0
        return item, self.next_true if passed_test else self.next_false


def run_rounds(data: str, n_rounds: int) -> list[Monkey]:
    monkeys = {m.id: m for m in [Monkey.parse(m) for m in data.split('Monkey ') if m]}

    def run_round():
        for monkey in monkeys.values():
            logger.debug(f'Turn: monkey {monkey.id}')
            for item, pass_to in monkey.inspect_items():
                recipient = monkeys[pass_to]
                recipient.items.append(item)
                logger.debug(f'  Passed item with value {item} to monkey {pass_to}')

    for i in range(n_rounds):
        run_round()
        logger.debug(f'Round {i}:')
        for monkey in monkeys.values():
            logger.debug(f'  Monkey {monkey.id}: {monkey.items_str}')

    return monkeys


def monkey_business(monkeys: list[Monkey]) -> int:
    sorted_monkeys = sorted(monkeys.values(), key=lambda m: m.n_inspected, reverse=True)
    return sorted_monkeys[0].n_inspected * sorted_monkeys[1].n_inspected


if __name__ == '__main__':
    data = read_input('11a')
    monkeys = run_rounds(data, 20)
    logger.info(f'Part 1: {monkey_business(monkeys)}')
