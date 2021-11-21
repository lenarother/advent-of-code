"""Day 23: Safe Cracking

https://adventofcode.com/2016/day/23

Part 2: Assembunny hack
"""


def loop(a, b):
    d = a
    a = 0
    a += b * d
    b -= 1
    c = b
    d = c
    c += d
    d = 0
    return a, b, c, d


def main():
    a, b = 12, 0
    b = a
    b -= 1
    a, b, c, d = loop(a, b)
    while c:
        a, b, c, d = loop(a, b)
    a += 72 * 75
    return a


if __name__ == '__main__':
    result = main()
    print(f'A: {result}')