"""Day 25: Full of Hot Air

https://adventofcode.com/2022/day/25

"""
DIGIT_MAP = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

ARABIC = [0, 1, 2, 3, 4]
SNAFU = ['0', '1', '2', '1=', '1-']
ARABIC_SNAFU = dict(zip(ARABIC, SNAFU))


def snafu_to_decimal(snafu):
    return sum(
        (5 ** n) * DIGIT_MAP[v]
        for n, v in enumerate(reversed(snafu))
    )


def decimal_to_snafu(decimal):
    result = ''

    # foo = decimal // 5
    # bar = decimal % 5
    # if foo > 5:
    #     result += decimal_to_snafu(foo)
    # else:
    #     result += ARABIC_SNAFU[foo]
    # result += ARABIC_SNAFU[bar]
    # result = result.lstrip('0')
    # return result
    foo = ''
    if decimal >= 5:
        foo += decimal_to_snafu(decimal // 5)
    foo += ARABIC_SNAFU[decimal % 5]
    return foo
    #print(decimal % 5, end = '')

def solve(data):
    n = sum(snafu_to_decimal(i) for i in data.strip().split('\n'))
    return n


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
