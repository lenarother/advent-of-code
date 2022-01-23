"""Day 2: 1202 Program Alarm

https://adventofcode.com/2019/day/2

"""

# memory address -> int index
# optcode -> first int in instructions,
#            1 (sum) | 2 (multi) | 99 (end)
# instruction -> optcode, param, param, param
# instruction pointer -> address of current instruction

import operator


class Game:

    def __init__(self, data):
        self.data = list(map(int, data.split(',')))
        self.position = 0

    def prepare_input(self, a, b):
        self.data[1] = a
        self.data[2] = b

    @property
    def operator(self):
        if self.data[self.position] == 1:
            return operator.add
        elif self.data[self.position] == 2:
            return operator.mul
        elif self.data[self.position] == 99:
            return False

    @property
    def val_a(self):
        return self.data[self.data[self.position + 1]]

    @property
    def val_b(self):
        return self.data[self.data[self.position + 2]]

    @property
    def target(self):
        return self.data[self.position + 3]

    @property
    def is_finished(self):
        return self.operator is False

    def step(self):
        if self.operator:
            self.data[self.target] = self.operator(self.val_a, self.val_b)
        self.position += 4

    def solve(self, prepare_input=False, a=12, b=2):
        if prepare_input:
            self.prepare_input(a, b)

        while not self.is_finished:
            self.step()

        return self.data[0]


def solve(data):
    return Game(data).solve(True)


def solve2(data):
    for noun in range(1, 100):
        for verb in range(1, 100):
            if Game(data).solve(True, noun, verb) == 19690720:
                return 100 * noun + verb
    return 0


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
