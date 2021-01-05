"""Day 18: Operation Order

https://adventofcode.com/2020/day/18

"""

from functools import reduce


def parse(expression):
    if isinstance(expression, str):
        expression = expression.split()
    result = []

    while len(expression) > 0:
        x = expression.pop(0)
        if not ('(' in x or ')' in x):
            result.append(x)
        elif '(' in x:
            x = x[1:]
            result_x, expression = parse([x] + expression)
            result.append(result_x)
        elif ')' in x:
            x, rest = x.split(')', 1)
            if x:
                result.append(x)
            if rest:
                expression = [rest] + expression
            return result, expression

    return result, []


def calculate_partial(expression):
    # Part 1
    # no brackets
    # e.g. ['7', '*', '3', '*', '3', '+', '9', '*', '3']
    while len(expression) > 1:
        result = str(eval(' '.join(expression[:3])))
        expression = [result] + expression[3:]
    return int(expression[0])


def calculate_partial_advanced(expression):
    # Part 2
    # no brackets
    # e.g. ['7', '*', '3', '*', '3', '+', '9', '*', '3']
    expression_str = ''.join(expression)
    expression = expression_str.split('*')
    result = []
    for x in expression:
        if '+' in x:
            result.append(eval(x))
        else:
            result.append(int(x))

    return reduce((lambda x, y: x * y), result)


def calculate(expression, advanced=False):
    flat = False

    while not flat:
        flat = True
        for counter, x in enumerate(expression):
            if isinstance(x, list):
                flat = False
                expression[counter] = calculate(x, advanced)

    if advanced:
        return str(calculate_partial_advanced(expression))
    return str(calculate_partial(expression))


def solve_expression(expression, advanced=False):
    parsed, _ = parse(expression)
    return int(calculate(parsed, advanced))


def sum_expression_results(filename, advanced=False):
    return sum([solve_expression(e, advanced) for e in open(filename).readlines()])


if __name__ == '__main__':

    # Part 1
    assert solve_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
    assert solve_expression('2 * 3 + (4 * 5)') == 26
    assert solve_expression('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    assert solve_expression('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    assert solve_expression('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert solve_expression('1 + (2 * 3) + (4 * (5 + 6))') == 51

    result = sum_expression_results('inputdata/day-18-1.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = sum_expression_results('inputdata/day-18-1.txt', advanced=True)
    print('Part 2 - Result: ', result)
