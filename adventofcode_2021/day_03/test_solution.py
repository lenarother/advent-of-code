import pytest

from .solution import (
    find_co2,
    find_most_common_bits,
    find_oxygen,
    parse_data,
    reverse_bitstring,
    solve,
    solve2,
)

DATA = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

EXAMPLES = (
    (DATA, '10110'),
)

EXAMPLES2 = (
    (DATA, 198),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_find_most_common(data, expected):
    data = parse_data(data)
    assert find_most_common_bits(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_reverse_bitstring(data, expected):
    assert reverse_bitstring('10110') == '01001'


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve(data, expected):
    assert solve(data) == expected


def test_find_oxygen():
    assert find_oxygen(DATA) == 23


def test_find_co2():
    assert find_co2(DATA) == 10


def test_solve2():
    assert solve2(DATA) == 230
