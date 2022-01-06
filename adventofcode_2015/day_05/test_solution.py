import pytest

from .solution import is_nice, is_nice2

EXAMPLES = (
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False),
)

EXAMPLES2 = (
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', False),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_is_nice(data, expected):
    assert is_nice(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_is_nice2(data, expected):
    assert is_nice2(data) == expected
