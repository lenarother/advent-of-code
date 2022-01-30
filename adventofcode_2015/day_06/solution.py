"""Day 6: Probably a Fire Hazard

https://adventofcode.com/2015/day/6

"""
import re
from abc import ABC, abstractmethod
from collections import defaultdict

INSTRUCTION = r'(turn|toggle) (on|off)?\s?(\d+),(\d+) through (\d+),(\d+)'


class Instruction(ABC):

    def __init__(self, i):
        self.points = points(
            (int(i[2]), int(i[3])),
            (int(i[4]), int(i[5]))
        )

    @abstractmethod
    def apply(self, data):
        raise NotImplementedError

    @abstractmethod
    def apply2(self, data):
        raise NotImplementedError


class TurnOn(Instruction):

    def apply(self, data):
        for p in self.points:
            data[p] = 1

    def apply2(self, data):
        for p in self.points:
            data[p] += 1


class TurnOff(Instruction):

    def apply(self, data):
        for p in self.points:
            data.pop(p, None)

    def apply2(self, data):
        for p in self.points:
            if p in data and data[p] > 0:
                data[p] -= 1


class Toggle(Instruction):

    def apply(self, data):
        for p in self.points:
            if p in data:
                data.pop(p)
            else:
                data[p] = 1

    def apply2(self, data):
        for p in self.points:
            data[p] += 2


def instructions(data):
    for i in re.findall(INSTRUCTION, data):
        match i[0]:
            case 'turn':
                yield TurnOff(i) if i[1] == 'off' else TurnOn(i)
            case 'toggle':
                yield Toggle(i)


def points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            yield x, y


def solve(data):
    lights = defaultdict(int)
    for i in instructions(data):
        i.apply(lights)
    return sum(lights.values())


def solve2(data):
    # TODO: solve and solve2 are redundant
    lights = defaultdict(int)
    for i in instructions(data):
        i.apply2(lights)
    return sum(lights.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
