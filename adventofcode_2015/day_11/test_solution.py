import pytest

from .solution import is_valid, passwords, prepare_input, solve

EXAMPLES = (
    ('a', 1, 'b'),
    ('a', 22, 'z'),
    ('h', 1, 'j'),
    ('k', 1, 'm'),
    ('n', 1, 'p'),
    ('abc', 1, 'abd'),
    ('abc', 2, 'abe'),
    ('azz', 1, 'baa'),
    ('zzz', 1, 'aaa'),
    ('abcaabf', 2, 'abcaabh'),
    ('aaaaaaaa', 1, 'aaaaaaab'),
    ('aaaaaaaz', 1, 'aaaaaaba'),
    ('azzzzzzz', 1, 'baaaaaaa'),
)
EXAMPLES_NEXT = (
    ('abcdefgh', 'abcdffaa'),
    ('ghjaabcb', 'ghjaabcc'),
    ('ghijklmn', 'ghjaabcc'),
)
EXAMPLES_VALID = (
    ('ghjaabcc', True),
)
EXAMPLES_PREPARE = (
    ('abcdefgh', 'abcdefgh'),
    ('ghjaabcb', 'ghjaabcb'),
    ('ohijklln', 'paaaaaaa'),
)


@pytest.mark.parametrize('passwd,steps,expected', EXAMPLES)
def test_passwords(passwd, steps, expected):
    passwd_gen = passwords(prepare_input(passwd))
    while steps:
        new_passwd = next(passwd_gen)
        steps -= 1
    assert new_passwd == expected


@pytest.mark.parametrize('passwd,expected', EXAMPLES_VALID)
def test_is_valid(passwd, expected):
    assert is_valid(passwd) == expected


@pytest.mark.parametrize('passwd,expected', EXAMPLES_PREPARE)
def test_prepare_input(passwd, expected):
    assert prepare_input(passwd) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_NEXT)
def test_solve(data, expected):
    assert solve(data) == expected
