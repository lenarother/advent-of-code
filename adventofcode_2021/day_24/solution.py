"""Day 24: Arithmetic Logic Unit

https://adventofcode.com/2021/day/24

"""
import re

INSTRUCTION = r'(inp|mul|add|mod|div|eql) (w|x|y|z)(.*)\n'

# steps 14 .. 1
PARAMS = [
    (26, -14, 10), (26, -8, 4), (26, -1, 15), (1, 14, 9),
    (1, 14, 6), (26, -15, 12), (26, -4, 13), (26, -11, 8),
    (1, 15, 12), (1, 13, 9), (26, -8, 10), (1, 15, 14),
    (1, 13, 14), (1, 11, 6)
]
RANGE_SIZE = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 2, 1, 1]


def run_monad(data, input_str):
    input_list = list(input_str)
    wxyz = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    def get_val(a):
        a = a.strip()
        if a in 'wxyz':
            return wxyz[a]
        return int(a)

    OPERATIONS = {
        'inp': lambda a, b: int(b.pop(0)),
        'mul': lambda a, b: get_val(a) * get_val(b),
        'add': lambda a, b: get_val(a) + get_val(b),
        'div': lambda a, b: get_val(a) // get_val(b),
        'eql': lambda a, b: int(get_val(a) == get_val(b)),
        'mod': lambda a, b: get_val(a) % get_val(b),
    }

    for i in re.findall(INSTRUCTION, data):
        inst, a, b = i
        if b == '':
            b = input_list
            print(wxyz['z'])
        wxyz[a] = OPERATIONS[inst](a, b)

    print(wxyz['z'])
    return tuple(wxyz.values())


def hashing_function(input_digit, z, param1, param2, param3):
    x = int(((z % 26) + param2) != input_digit)
    z = z // param1
    if x:
        z = (26 * z) + input_digit + param3
    return z


def run_monad_simplified(input_str):
    z = 0
    for w, p in zip(input_str, reversed(PARAMS)):
        z = hashing_function(int(w), z, *p)
    return z


class Step:

    def __init__(self, expected_solutions, params, z_range, w_range=None):
        self.expected_solutions = expected_solutions
        self.params = params
        self.z_range = range(26 ** z_range + 1)
        self.w_range = w_range or range(1, 10)
        self.solutions_dict = {}
        self.solutions_set = set()

    def check_solution(self, input_digit, input_z):
        p1, p2, p3 = self.params
        output_z = hashing_function(input_digit, input_z, p1, p2, p3)
        if output_z in self.expected_solutions:
            self.solutions_set.add(input_z)
            self.solutions_dict[input_z] = (input_digit, output_z)

    def find_solutions(self):
        for input_z in self.z_range:
            for input_digit in self.w_range:
                self.check_solution(input_digit, input_z)


def solve(w_range=None):
    steps = []
    expected_solutions = {0}
    for p, r_size in zip(PARAMS, RANGE_SIZE):
        s = Step(expected_solutions, p, r_size, w_range)
        s.find_solutions()
        steps.append(s)
        expected_solutions = s.solutions_set

    result_code = ''
    expected_output = 0
    while steps:
        s = steps.pop()
        input_digit, expected_output = s.solutions_dict[expected_output]
        result_code += str(input_digit)

    return result_code


if __name__ == '__main__':
    result = solve()
    print(f'Example1: {result}')

    result = solve(w_range=range(9, 0, -1))
    print(f'Example2: {result}')
