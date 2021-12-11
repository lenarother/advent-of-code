import pytest

from .solution import Octopus, solve, solve2

DATA = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

DATA_SMALL = """
11111
19991
19191
19991
11111"""

DATA_SMALL_SIMPLE = """
11111
11111
11911
11111
11111"""

EXAMPLES = (
    (DATA_SMALL_SIMPLE, 1, 1),
    (DATA_SMALL, 0, 0),
    (DATA_SMALL, 2, 9),
    (DATA, 1, 0),
    (DATA, 2, 35),
    (DATA, 100, 1656),
)

EXAMPLES_POSITION = (
    (DATA_SMALL, (0, 0), {(1, 0), (0, 1), (1, 1)}),
    (
        DATA_SMALL,
        (2, 2),
        {(2, 3), (2, 1), (3, 2), (1, 2), (1, 3), (3, 3), (1, 1), (3, 1)}),
)

EXAMPLES_REPR = (
    DATA_SMALL,
    DATA,
)

EXAMPLES_FIND_FLASH = (
    (DATA, 195),
)


@pytest.mark.parametrize('data,pos,expected', EXAMPLES_POSITION)
def test_positions(data, pos, expected):
    octopus = Octopus(data)
    assert set(octopus.get_adj_positions(pos)) == expected


@pytest.mark.parametrize('data', EXAMPLES_POSITION)
def test_repr(data):
    data = data[0].strip()
    assert f'{Octopus(data)}' == data


@pytest.mark.parametrize('data,steps,expected', EXAMPLES)
def test_solve(data, steps, expected):
    assert solve(data, steps) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_FIND_FLASH)
def test_solve2(data, expected):
    assert solve2(data) == expected
