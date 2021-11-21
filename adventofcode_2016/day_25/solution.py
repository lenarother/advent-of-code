"""Day 25: Clock Signal

https://adventofcode.com/2016/day/25

"""
import re
from collections import OrderedDict
from itertools import count

CPY = r'cpy (-?)(\d+|[abcd]) ([abcd])'  # 2
DEC = r'dec ([abcd])'  # 1
INC = r'inc ([abcd])'  # 1
JNZ = r'jnz (\d+|[abcd]) (-?)(\d+|[abcd])'  # 2
OUT = r'out (-?)(\d+|[abcd])'  # 1
TGL = r'tgl (-?)(\d+|[abcd])'  # 1


class Parser:

    @staticmethod
    def parse_value(v, sign=None):
        return int(v) * (-1 if sign else 1) if v.isnumeric() else v

    @staticmethod
    def cpy(instruction):
        sign, v, target = re.findall(CPY, instruction)[0]
        return Parser.parse_value(v, sign), target

    @staticmethod
    def inc(instruction):
        return tuple(re.findall(INC, instruction))

    @staticmethod
    def dec(instruction):
        return tuple(re.findall(DEC, instruction))

    @staticmethod
    def jnz(instruction):
        check, sign, jump = re.findall(JNZ, instruction)[0]
        return Parser.parse_value(check), Parser.parse_value(jump, sign)

    @staticmethod
    def tgl(instruction):
        sign, v = re.findall(TGL, instruction)[0]
        return Parser.parse_value(v, sign),

    @staticmethod
    def out(instruction):
        sign, v = re.findall(OUT, instruction)[0]
        return Parser.parse_value(v, sign),

    @staticmethod
    def parse(data):
        instructions = {}
        for counter, instruction in enumerate(data.split('\n')):
            name = instruction[:3]
            parser = getattr(Parser, name)
            instructions[counter] = {
                'name': name,
                'values': parser(instruction)
            }
        return instructions


class Solver:

    def __init__(self, data, a=0):
        self.a = a
        self.instructions = Parser.parse(data)
        self.values = OrderedDict({
            'a': a,
            'b': 0,
            'c': 0,
            'd': 0
        })
        self.counter = 0
        self.solver_output = ''

    def get_value(self, v):
        return self.values[v] if isinstance(v, str) else v

    def cpy(self, v, target):
        self.values[target] = self.get_value(v)
        self.counter += 1

    def inc(self, target):
        self.values[target] += 1
        self.counter += 1

    def dec(self, target):
        self.values[target] -= 1
        self.counter += 1

    def out(self, x):
        self.solver_output += str(self.get_value(x))
        self.counter += 1

    def jnz(self, check, jump):
        check = self.get_value(check)
        jump = self.get_value(jump)
        self.counter += jump if check else 1

    def tgl(self, v):
        v = self.get_value(v)
        c = self.counter + v
        self.counter += 1

        if c not in self.instructions:
            return

        name = self.instructions[c]['name']
        args_count = len(self.instructions[c]['values'])
        if args_count == 1 and name == 'inc':
            self.instructions[c]['name'] = 'dec'
        elif args_count == 1:
            self.instructions[c]['name'] = 'inc'
        elif args_count == 2 and name == 'jnz':
            self.instructions[c]['name'] = 'cpy'
        elif args_count == 2:
            self.instructions[c]['name'] = 'jnz'

    def solve_instruction(self):
        inst = self.instructions[self.counter]
        solver = getattr(self, inst['name'])
        try:
            solver(*inst['values'])
        except KeyError:
            self.counter += 1

    def check_output(self):
        expected1 = '101010101010101010101010101010101010'
        expected2 = '010101010101010101010101010101010101'
        return (
            (self.solver_output == expected1) or
            (self.solver_output == expected2)
        )

    def solve(self):
        x = 0
        while self.counter in self.instructions:
            self.solve_instruction()
            if x == 100_000:
                break
            x += 1
        if self.solver_output:
            return self.check_output()


def solve(data):
    for a in count():
        s = Solver(data, a).solve()
        if s:
            return a


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data)
    print(f'Example1: {result}')
