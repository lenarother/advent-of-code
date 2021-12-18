"""Day 18: Snailfish

https://adventofcode.com/2021/day/18

"""
import itertools
import re
from collections import deque


class Reducer:

    @staticmethod
    def rreplace(s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

    def _explode_left(self, left_part, lch):
        numbers = re.findall(r'\d+', left_part)
        if not numbers:
            return left_part

        n = numbers[-1]
        new_n = int(n) + int(lch)

        return self.rreplace(left_part, n, f'{new_n}', 1)

    def _explode_right(self, right_part, rch):
        numbers = re.findall(r'\d+', right_part)
        if not numbers:
            return right_part

        n = numbers[0]
        new_n = int(n) + int(rch)

        return right_part.replace(n, f'{new_n}', 1)

    def explode_expr(self, expr):
        expr = deque(expr)
        left_part = ''
        open_count = 0
        while expr:

            ch = expr.popleft()
            if ch == '[':
                open_count += 1
            elif ch == ']':
                open_count -= 1

            if open_count == 5:
                right_part = ''.join(expr)
                lch, right_part = right_part.split(',', 1)
                rch, right_part = right_part.split(']', 1)
                new_left = self._explode_left(left_part, lch)
                new_right = self._explode_right(right_part, rch)
                return new_left + '0' + new_right

            left_part += ch
        return left_part

    def split_expr(self, expr):
        numbers = deque(re.findall(r'\d+', expr))
        while numbers:
            n = numbers.popleft()
            if int(n) >= 10:
                n_new = f'[{int(n) // 2},{(int(n) // 2) + (int(n) % 2)}]'
                return expr.replace(n, n_new, 1)
        return expr

    def _reduce_explode(self, expr):
        while 1:
            new_expr = self.explode_expr(expr)
            if new_expr == expr:
                return new_expr
            expr = new_expr

    def reduce_expression(self, expr):
        while 1:
            expr = self._reduce_explode(expr)
            new_expr = self.split_expr(expr)
            if new_expr == expr:
                return new_expr
            expr = new_expr


def add_expr(expr1, expr2):
    expr_sum = str([eval(expr1)] + [eval(expr2)]).replace(' ', '')
    return Reducer().reduce_expression(expr_sum)


def find_sum(data):
    expressions = data.strip().split('\n')
    expr = expressions[0]
    for i in range(1, len(expressions)):
        expr = add_expr(expr, expressions[i])
    return expr


def calc_magnitude(expr):
    expr = eval(expr)

    l_expr = expr[0]
    if not isinstance(l_expr, int):
        l_expr = calc_magnitude(str(l_expr))

    r_expr = expr[1]
    if not isinstance(r_expr, int):
        r_expr = calc_magnitude(str(r_expr))

    return (3 * l_expr) + (2 * r_expr)


def find_max_magnitude(data):
    mag = 0
    expressions = data.strip().split('\n')
    for e1, e2 in itertools.combinations(expressions, 2):
        mag_1 = calc_magnitude(add_expr(e1, e2))
        mag_2 = calc_magnitude(add_expr(e2, e1))
        mag = max(mag, mag_1, mag_2)
    return mag


def solve(data):
    expr_sum = find_sum(data)
    return calc_magnitude(expr_sum)


def solve2(data):
    return find_max_magnitude(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
