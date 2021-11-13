import pytest

from .solution import solve

EXAMPLES = (
    ('abcde', 'swap position 4 with position 0', 'ebcda'),
    ('abcde', 'swap position 1 with position 2', 'acbde'),
    ('abcde', 'swap position 1 with position 4', 'aecdb'),
    ('abcde', 'swap letter a with letter b', 'bacde'),
    ('abcde', 'swap letter b with letter a', 'bacde'),
    ('abcde', 'rotate right 1 steps', 'eabcd'),
    ('abcde', 'rotate right 3 steps', 'cdeab'),
    ('abcde', 'rotate right 6 steps', 'eabcd'),
    ('abcde', 'rotate left 1 steps', 'bcdea'),
    ('abcde', 'rotate left 3 steps', 'deabc'),
    ('abcde', 'rotate left 6 steps', 'bcdea'),
    ('abcde', 'reverse positions 0 through 4', 'edcba'),
    ('abcde', 'reverse positions 0 through 3', 'dcbae'),
    ('abcde', 'reverse positions 1 through 3', 'adcbe'),
    ('abcde', 'move position 1 to position 2', 'acbde'),
    ('abcde', 'move position 1 to position 4', 'acdeb'),
)

EXAMPLES_IRREVERSIBLE = (
    ('abcde', 'rotate based on position of letter a', 'eabcd'),
    ('abcde', 'rotate based on position of letter b', 'deabc'),
    ('abcde', 'rotate based on position of letter e', 'eabcd'),
    ('abcde', """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""", 'decab'),
)

EXAMPLES_REVERSIBLE = (
    ('abcdefgh', 'rotate based on position of letter a', 'habcdefg'),
    ('abcdefgh', 'rotate based on position of letter b', 'ghabcdef'),
    ('abcdefgh', 'rotate based on position of letter c', 'fghabcde'),
    ('abcdefgh', 'rotate based on position of letter d', 'efghabcd'),
    ('abcdefgh', 'rotate based on position of letter e', 'cdefghab'),
)


@pytest.mark.parametrize(
    'input_str,rule,expected',
    EXAMPLES + EXAMPLES_IRREVERSIBLE
)
def test_solve(input_str, rule, expected):
    assert solve(input_str, rule) == expected


@pytest.mark.parametrize(
    'expected,rules,pwd',
    EXAMPLES + EXAMPLES_REVERSIBLE
)
def test_solve_reverse(expected, rules, pwd):
    assert solve(pwd, rules, reverse=True) == expected
