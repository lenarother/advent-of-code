"""Day 20: Infinite Elves and Infinite Houses

https://adventofcode.com/2015/day/20

"""
from collections import defaultdict


def solve(present_count):
    n = 1
    results = defaultdict(list)

    while n:
        current_result = results.pop(n, [])
        current_result.append(n)

        if sum(current_result) * 10 >= present_count:
            return n

        for i in current_result:
            results[i + n].append(i)
        n += 1


def solve2(present_count):
    n = 1
    results = defaultdict(list)
    houses_count = defaultdict(int)

    while n:
        current_result = results.pop(n, [])
        current_result.append(n)

        if sum(current_result) * 11 >= present_count:
            return n

        for i in current_result:
            houses_count[i] += 1
            if houses_count[i] <= 50:
                results[i + n].append(i)

        n += 1


if __name__ == '__main__':
    result = solve(29_000_000)
    print(f'Example1: {result}')

    result = solve2(29_000_000)
    print(f'Example2: {result}')
