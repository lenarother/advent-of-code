import pytest

from .solution import (
    find_co2,
    find_most_common_bits,
    find_oxygen,
    parse_data,
    reverse_bitstring,
    solve,
    solve2,
    transpose_list,
)

DATA_SMALL = """
00100
11110
10110"""

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
    (DATA_SMALL, '10110'),
    (DATA, '10110'),
)

EXAMPLES_SOLVE = (
    (DATA_SMALL, 198),
    (DATA, 198),
)

EXAMPLES_REVERSE = (
    ('0', '1'),
    ('00000', '11111'),
    ('11111', '00000'),
    ('10110', '01001'),
)

EXAMPLES_TRANSPOSE = (
    (['11', '22', '33'], [['1', '2', '3'], ['1', '2', '3']]),
    ([['1', '1'], ['2', '2'], ['3', '3']], [['1', '2', '3'], ['1', '2', '3']]),
)


@pytest.mark.parametrize('data,expected', EXAMPLES_TRANSPOSE)
def test_transpose_list(data, expected):
    assert transpose_list(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_find_most_common(data, expected):
    data = parse_data(data)
    assert find_most_common_bits(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_REVERSE)
def test_reverse_bitstring(data, expected):
    result = reverse_bitstring(data)
    assert result == expected
    assert reverse_bitstring(result) == data  # round trip


@pytest.mark.parametrize('data,expected', EXAMPLES_SOLVE)
def test_solve(data, expected):
    assert solve(data) == expected


def test_find_oxygen():
    assert find_oxygen(DATA) == 23


def test_find_co2():
    assert find_co2(DATA) == 10


def test_solve2():
    assert solve2(DATA) == 230
