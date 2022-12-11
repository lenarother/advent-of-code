"""Day 11: Monkey in the Middle

https://adventofcode.com/2022/day/11

"""
import operator
import re
from collections import deque
from functools import reduce

MONKEY = re.compile(
    r'Monkey (?P<id>\d+):\n\s*Starting items: (?P<items>[0-9,\s]*)\n\s*'
    r'Operation: new = old (?P<operation_type>[+*]) '
    r'(?P<operation_value>\d+|old)\n\s*Test: divisible by '
    r'(?P<divisible>\d+)\n\s*If true: throw to monkey '
    r'(?P<test_true>\d+)\n\s*If false: throw to monkey (?P<test_false>\d+)'
)


class Monkey:
    def __init__(
        self,
        id,
        operation_type,
        operation_value,
        divisible,
        test_true,
        test_false,
        items=[],
    ):
        self.id = id
        self.operation_type = operation_type
        self.operation_value = operation_value
        self.divisible = divisible
        self.test_true = test_true
        self.test_false = test_false
        self.items = items
        self.count = 0
        self.reduce_worry_level = True
        self.least_common_multiple = None

    def __repr__(self):
        return f'<Monkey: {self.id}>'

    def find_new_worry_level(self, worry_level):
        value = self.operation_value or worry_level
        new_worry_level = self.operation_type(worry_level, value)
        if self.reduce_worry_level:
            return new_worry_level // 3
        return new_worry_level % self.least_common_multiple

    def find_target(self, worry_level):
        self.count += 1
        if worry_level % self.divisible == 0:
            return self.test_true
        return self.test_false


def parse(data):
    monkeys = {}
    operations = {'+': operator.add, '*': operator.mul}
    for m in MONKEY.finditer(data):
        monkey = Monkey(**m.groupdict())
        monkey.operation_type = operations.get(monkey.operation_type)
        monkey.operation_value = (
            int(monkey.operation_value)
            if monkey.operation_value.isdigit()
            else None
        )
        monkey.items = deque(list(map(int, monkey.items.strip().split(', '))))
        monkey.divisible = int(monkey.divisible)
        monkeys[monkey.id] = monkey
    return monkeys


def throw_round(monkeys):
    for m in monkeys.values():
        while m.items:
            item = m.items.popleft()
            worry_level = m.find_new_worry_level(item)
            target = m.find_target(worry_level)
            monkey = monkeys[target]
            monkey.items.append(worry_level)


def prepare_input(monkeys, reduce_worry_level):
    least_common_multiple = reduce(
        operator.mul,
        [m.divisible for m in monkeys.values()]
    )
    for m in monkeys.values():
        m.reduce_worry_level = reduce_worry_level
        m. least_common_multiple = least_common_multiple


def solve(monkeys, n=20, reduce_worry_level=True):
    monkeys = parse(monkeys)
    prepare_input(monkeys, reduce_worry_level)
    for i in range(n):
        throw_round(monkeys)
    count = sorted([m.count for m in monkeys.values()], reverse=True)
    return count[0] * count[1]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 10000, False)
    print(f'Example2: {result}')
