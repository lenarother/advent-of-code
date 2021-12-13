"""Day 8: Seven Segment Search

https://adventofcode.com/2021/day/8

"""
from collections import deque
# intersection len. 1, 4
# DIGIT_DEFINITION = {
#     1: (2, 2, 2),
#     2: (2, 2, 2),
# }
def get_sets_diff_len(k, code, digit_code):
    return len(set(digit_code[k]) - set(code))


def parse_digits(digits_sting):
    digit_code = {}
    codes = deque(sorted(digits_sting.strip().split(), key=len))

    digit_code[1] = codes.popleft()
    digit_code[7] = codes.popleft()
    digit_code[4] = codes.popleft()
    digit_code[8] = codes.pop()

    while codes:
        code = codes.pop()
        if len(code) == 6 and get_sets_diff_len(1, code, digit_code) == 1:
            digit_code[6] = code
            continue
        elif len(code) == 6 and get_sets_diff_len(4, code, digit_code) == 0:
            digit_code[9] = code
            continue
        elif len(code) == 6:
            digit_code[0] = code
            continue
        elif len(code) == 5 and get_sets_diff_len(1, code, digit_code) == 0:
            digit_code[3] = code
            continue
        elif len(code) == 5 and get_sets_diff_len(4, code, digit_code) == 2:
            digit_code[2] = code
            continue
        elif len(code) == 5:
            digit_code[5] = code
            continue
    return {
        ''.join(sorted(code)): str(digit)
        for digit, code in digit_code.items()
    }


def calc_line(line):
    digit_string, task = line.split(' | ')
    code_digit = parse_digits(digit_string)
    return int(''.join([
        code_digit[''.join(sorted(code))]
        for code in task.strip().split()
    ]))


def solve2(data):
    all_nums = []
    for line in data.strip().split('\n'):
        all_nums.append(calc_line(line))
    return sum(all_nums)


def solve(data):
    possible_lengths = [2, 4, 3, 7]
    count = 0
    for line in data.strip().split('\n'):
        after = line.split(' | ')[1]
        digits = after.split()
        for d in digits:
            if len(d) in possible_lengths:
                count += 1
    return count


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print(f'Example2: {result}')