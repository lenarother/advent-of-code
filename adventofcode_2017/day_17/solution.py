"""Day 17: Spinlock

https://adventofcode.com/2017/day/17

"""


def spinlock(step):
    position = 0
    buffer = [0]
    value = 1
    while 1:
        position = ((position + step) % value) + 1
        buffer = buffer[:position] + [value] + buffer[position:]
        value += 1
        yield buffer


def solve(step=304, n=2017):
    s = spinlock(step)
    while n:
        buffer = next(s)
        n -= 1
    i = buffer.index(2017)
    return buffer[i + 1]


def spinlock2(step):
    position = 0
    current_result = 1
    value = 1
    while 1:
        position = ((position + step) % value) + 1
        if position == 1:
            current_result = value
        value += 1
        yield current_result


def solve2(step=304, n=1):
    s = spinlock2(step)
    while n:
        value = next(s)
        n -= 1
    return value


if __name__ == '__main__':
    result = solve()
    print(f'Example1: {result}')

    result = solve2(n=50_000_000)
    print(f'Example2: {result}')
