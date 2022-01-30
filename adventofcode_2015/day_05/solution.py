"""Day 5: Doesn&apos;t He Have Intern-Elves For This?

https://adventofcode.com/2015/day/5

"""
import re

DUPLICATES = r'(\w)\1+'
VOWELS = r'([a|e|i|o|u])'
MUST_NOT_HAVE = r'(ab|cd|pq|xy)'

REPEAT_WITH_LETTER_IN_BETWEEN = r'(\w)\w\1'
PAIR = r'(\w\w)\w*\1'

# TODO: single is_nice and list of condition wit any / all
# TODO: return at the begining


def is_nice(word):
    if (
            not any(re.findall(DUPLICATES, word)) or
            not len(re.findall(VOWELS, word)) >= 3 or
            any(re.findall(MUST_NOT_HAVE, word))
    ):
        return False
    return True


def is_nice2(word):
    if (
            not any(re.findall(REPEAT_WITH_LETTER_IN_BETWEEN, word)) or
            not any(re.findall(PAIR, word))
    ):
        return False
    return True


def solve(data, is_nice_function=is_nice):
    return sum([is_nice_function(w) for w in data.strip().split('\n')])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, is_nice2)
    print(f'Example2: {result}')
