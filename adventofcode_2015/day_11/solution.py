"""Day 11: Corporate Policy

https://adventofcode.com/2015/day/11

"""
import re

PASS_LETTERS = 'abcdefghjkmnpqrstuvwxyz'
SKIP = {
    'i': 'j',
    'l': 'm',
    'o': 'p'
}

RE_REPETITION = re.compile(r'(.)\1')
RE_EXCLUDED = re.compile(r'i|l|o')
RE_INCREASING_TRIPLET = re.compile(
    r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz'
)


def prepare_input(passwd):
    """Skip i, l, o to avoid unnecessary iterations"""
    for i, ch in enumerate(passwd):
        if ch in SKIP:
            return passwd[:i] + SKIP[ch] + 'a' * (len(passwd) - i - 1)
    return passwd


def next_letter(ch):
    ch_index = PASS_LETTERS.index(ch)
    next_index = (ch_index + 1) % len(PASS_LETTERS)
    return PASS_LETTERS[next_index]


def passwords(initial_passwd):
    passwd = initial_passwd
    while 1:
        new_letters = ''
        do_update = True
        i = -1

        while do_update:
            new_ch = next_letter(passwd[i])
            new_letters = new_ch + new_letters
            i -= 1

            if new_ch != 'a' or abs(i) > len(passwd):
                do_update = False

        passwd = passwd[:(i + 1)] + new_letters
        if passwd == initial_passwd:
            return
        yield passwd


def is_valid(passwd):
    if RE_EXCLUDED.findall(passwd):
        return False
    if not RE_INCREASING_TRIPLET.findall(passwd):
        return False
    repeats = RE_REPETITION.findall(passwd)
    if len(repeats) < 2:
        return False
    if len(set(repeats)) == 1:
        return False
    return True


def find_next_valid_passwd(passwd):
    pgen = passwords(prepare_input(passwd))
    for p in pgen:
        if is_valid(p):
            return p


def solve(data):
    return find_next_valid_passwd(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(result)
    print(f'Example2: {result}')
