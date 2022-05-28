"""Day 13: Packet Scanners

https://adventofcode.com/2017/day/13

"""


def parse(data):
    return {
        int(k): int(v)
        for k, v in [
            linie.strip().split(': ')
            for linie in data.strip().split('\n')
        ]
    }


def is_caught(scan_range, t):
    if t == 0:
        return True
    return t % (scan_range * 2 - 2) == 0


def caught_layers(firewall, delay=0):
    return [
        layer for layer in firewall
        if is_caught(firewall[layer], layer + delay)
    ]


def has_caught_layers(firewall, delay=0):
    for layer in firewall:
        if is_caught(firewall[layer], layer + delay):
            return True
    return False


def solve(data):
    firewall = parse(data)
    return sum([
        layer * firewall[layer]
        for layer in caught_layers(firewall)
    ])


def solve2(data):
    firewall = parse(data)
    delay = 0
    while 1:
        if not has_caught_layers(firewall, delay):
            return delay
        delay += 1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
