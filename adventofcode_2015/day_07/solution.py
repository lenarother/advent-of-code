"""Day 7: Some Assembly Required

https://adventofcode.com/2015/day/7

"""
import re

BOOL_RE = {
    'Assignment': re.compile(r'^(\w+|\d+)$'),
    'And': re.compile(r'(\w+|\d+) AND (\w+|\d+)'),
    'Or': re.compile(r'(\w+|\d+) OR (\w+|\d+)'),
    'Lshift': re.compile(r'(\w+|\d+) LSHIFT (\w+|\d+)'),
    'Rshift': re.compile(r'(\w+|\d+) RSHIFT (\w+|\d+)'),
    'Not': re.compile(r'NOT (\w+|\d+)'),
}

BOOL_OPERATIONS = {
    'Assignment': lambda a: a,
    'And': lambda a, b: a & b,
    'Or': lambda a, b: a | b,
    'Lshift': lambda a, b: a << b,
    'Rshift': lambda a, b: a >> b,
    'Not': lambda a: 65535 - a,
}

# TODO: solve recursively
# TODO: move name and result to the Operation Class


class BoolOperation:

    def __init__(self, i):
        self.i = i
        self.pattern = None
        self.operation = None
        self._set_operation()

    def __repr__(self):
        return self.i

    def _set_operation(self):
        for name, pattern in BOOL_RE.items():
            if pattern.match(self.i):
                self.pattern = pattern
                self.operation = BOOL_OPERATIONS[name]
                return

    @staticmethod
    def _get_value(var, values):
        if var.isnumeric():
            return int(var)
        if var in values:
            return values[var]

    @staticmethod
    def _can_evaluate(params):
        return all([p is not None for p in params])

    def _get_params(self, values):
        parsed = self.pattern.findall(self.i)

        vals = []
        for x in parsed:
            if type(x) in [list, tuple]:
                vals.extend(list(x))
            else:
                vals.append(x)

        return [self._get_value(v, values) for v in vals]

    def eval(self, values):
        params = self._get_params(values)
        if self._can_evaluate(params):
            return self.operation(*params)


def parse(data):
    wires = {}
    for line in data.strip().split('\n'):
        inp, wire = line.split(' -> ')
        wires[wire] = BoolOperation(inp)
    return wires


def connect_wires(wires, wires_solved):
    for wire in list(wires.keys()):
        # TODO:
        # if wire.can_evaluate():
        #    solved[w] = wire.evaluate()

        wire_output = wires[wire].eval(wires_solved)
        if wire_output is not None:
            wires_solved[wire] = wire_output
            del wires[wire]


def solve(data, var):
    wires = parse(data)
    wires_solved = {}
    assert var in wires

    while var not in wires_solved:
        connect_wires(wires, wires_solved)

    return wires_solved[var]


def solve2(data, var):
    wires = parse(data)
    assert var in wires

    wires_solved = {'b': 16076}
    wires.pop('b')

    while var not in wires_solved:
        connect_wires(wires, wires_solved)

    return wires_solved[var]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, 'a')
    print(f'Example1: {result}')

    result = solve2(input_data, 'a')
    print(f'Example2: {result}')
