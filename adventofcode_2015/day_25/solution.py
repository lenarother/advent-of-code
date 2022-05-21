"""Day 25: Let It Snow

https://adventofcode.com/2015/day/25

"""


def code_generator():
    previous_code = None
    while 1:
        if not previous_code:
            yield 20151125
            previous_code = 20151125
        previous_code = (previous_code * 252533) % 33554393
        yield previous_code


def position_generator():
    x, y = 0, 0
    while 1:
        if y == 0:
            x = 1
            y = 1
        elif y == 1:
            y = x + 1
            x = 1
        else:
            y -= 1
            x += 1
        yield x, y


def solve(row, column):
    pg = position_generator()
    cg = code_generator()

    while 1:
        x, y = next(pg)
        c = next(cg)
        if x == column and y == row:
            return c


if __name__ == '__main__':
    result = solve(row=2947, column=3029)
    print(f'Example1: {result}')
