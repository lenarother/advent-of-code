"""title

https://adventofcode.com/2025/day/6

"""
import itertools
import math


def input_generator(data):
    data = data.strip().split('\n')
    first_line = data[0].strip().split()
    second_line = data[1].strip().split()
    third_line = data[2].strip().split()
    fourth_line = data[3].strip().split()
    fifth_line = data[4].strip().split()
    for a, b, c, d, sign in zip(
            first_line,
            second_line,
            third_line,
            fourth_line,
            fifth_line
    ):
        yield int(a), int(b), int(c), int(d), sign


def input_generator2(data):
    data = data.strip().split('\n')
    mya = ''
    myb = ''
    myc = ''
    myd = ''
    mysign = ''
    for a, b, c, d, sign in itertools.zip_longest(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            fillvalue=' '
    ):
        print(a, b, c, d)
        if all([a == ' ', b == ' ', c == ' ', d == ' ', sign == ' ']):
            yield mya, myb, myc, myd, mysign.strip()
            mya = ''
            myb = ''
            myc = ''
            myd = ''
            mysign = ''
        else:
            mya += ('0' if a == ' ' else a)
            myb += ('0' if b == ' ' else b)
            myc += ('0' if c == ' ' else c)
            myd += ('0' if d == ' ' else d)
            mysign += sign
    yield mya, myb, myc, myd, mysign.strip()


def solve(data):
    result = 0
    for a, b, c, d, sign in input_generator(data):
        if sign == "+":
            result += a + b + c + d
        elif sign == "*":
            result += a * b * c * d
    return result


def solve2(data):
    result = 0
    for a, b, c, d, sign in input_generator2(data):
        temp = {}
        for i in range(len(a)):
            temp[i] = int(f'{a[i]}{b[i]}{c[i]}{d[i]}'.replace('0', ''))
        if sign == "+":
            result += sum(temp.values())
        elif sign == "*":
            result += math.prod(temp.values())
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example1: {result}')
