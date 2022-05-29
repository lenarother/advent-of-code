"""Day 15: Dueling Generators

https://adventofcode.com/2017/day/15

"""


def base_generator(start_number, factor, condition=None):
    previous_value = start_number
    divider = 2147483647

    while 1:
        previous_value = (previous_value * factor) % divider
        if (not condition) or (condition and previous_value % condition == 0):
            yield previous_value


def hex_generator(gen):
    while 1:
        yield bin(next(gen))[2:].zfill(32)


def hex_16_generator(gen):
    while 1:
        yield next(gen)[-16:]


def compare_generator(ga, gb):
    while 1:
        yield next(ga) == next(gb)


def create_compare_gen(
        start_a=591,
        start_b=393,
        condition_a=None,
        condition_b=None
):
    factor_a = 16807
    factor_b = 48271
    return compare_generator(
        hex_16_generator(hex_generator(base_generator(start_a, factor_a, condition_a))),  # noqa
        hex_16_generator(hex_generator(base_generator(start_b, factor_b, condition_b))),  # noqa
    )


def solve(
        start_a=591,
        start_b=393,
        n=40_000_000,
        condition_a=None,
        condition_b=None
):
    counter = 0
    cg = create_compare_gen(start_a, start_b, condition_a, condition_b)
    while n:
        counter += next(cg)
        n -= 1
    return counter


if __name__ == '__main__':
    result = solve()
    print(f'Example1: {result}')

    result = solve(n=5_000_000, condition_a=4, condition_b=8)
    print(f'Example2: {result}')
