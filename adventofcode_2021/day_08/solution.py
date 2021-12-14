"""Day 8: Seven Segment Search

https://adventofcode.com/2021/day/8

"""
DIGIT_DEFINITION = {
    # (len, intersection 1, intersection 4): digit
    (6, 2, 3): '0',
    (2, 2, 2): '1',
    (5, 1, 2): '2',
    (5, 2, 3): '3',
    (4, 2, 4): '4',
    (5, 1, 3): '5',
    (6, 1, 3): '6',
    (3, 2, 2): '7',
    (7, 2, 4): '8',
    (6, 2, 4): '9',
}


def parse_line(line):
    all_digit_string, target_digits = line.split(' | ')
    all_digit_list = sorted(all_digit_string.strip().split(), key=len)
    digit_1 = all_digit_list[0]
    digit_4 = all_digit_list[2]
    return digit_1, digit_4, target_digits.split()


def get_digit(target_digit, digit_1, digit_4):
    return DIGIT_DEFINITION[(
        len(target_digit),
        len(set(target_digit).intersection(set(digit_1))),
        len(set(target_digit).intersection(set(digit_4))),
    )]


def calculate_num_from_line(line):
    digit_1, digit_4, target_digits = parse_line(line)
    return int(''.join([
        get_digit(d, digit_1, digit_4)
        for d in target_digits
    ]))


def solve2(data):
    return sum([
        calculate_num_from_line(line)
        for line in data.strip().split('\n')
    ])


def solve(data):
    count = 0
    for line in data.strip().split('\n'):
        count += sum([
            1 for d in line.split(' | ')[1].split()
            if len(d) in [2, 3, 4, 7]]
        )
    return count


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
