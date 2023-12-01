import pytest

from .solution import solve, get_num_from_line

DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

DATA_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


@pytest.mark.parametrize(
    'data,expected',
    (
        (DATA, 142),
        (DATA_2, 281),
    ),
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data,expected',
    (
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("eight3eight", 88),
    )
)
def test_get_num_from_line(data, expected):
    assert get_num_from_line(data) == expected