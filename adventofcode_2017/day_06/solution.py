"""Day 6: Memory Reallocation

https://adventofcode.com/2017/day/6

"""


def redistribute(banks):
    banks = list(banks)

    i = banks.index(max(banks))
    blocks = banks[i]
    add_to_all = blocks // len(banks)
    blocks_rest = blocks % len(banks)

    banks[i] = 0
    banks = [b + add_to_all for b in banks]
    while blocks_rest:
        i += 1
        banks[i % len(banks)] += 1
        blocks_rest -= 1

    return tuple(banks)


def solve(data):
    banks = tuple(map(int, data.strip().split()))
    visited = set()
    i = 0

    while banks not in visited:
        visited.add(tuple(banks))
        banks = redistribute(banks)
        i += 1

    print(banks)
    return i


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve('10 9 8 7 6 5 4 3 1 1 0 15 14 13 11 12')
    print(f'Example2: {result}')
