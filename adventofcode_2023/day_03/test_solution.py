import pytest

from .solution import solve, solve_2, get_neighbour_positions, get_position

DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

DATA_2 = """467..114..
...*.....1
*.35..633.
......#..*
617.......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
..........
..35*35..."""

EXAMPLES = (
    (DATA, 4361),
    (DATA_2, 4361 - 617 + 70),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'n, expected',
    (
        ('114', {4, 8, 14, 15, 16, 17, 18}),
    )
)
def test_get_neighbour(n, expected):
    data = DATA.replace('\n', '')
    ln = len(DATA.split("\n")[0])
    ind = data.index(n)
    x, y = get_position(ind, ln)
    assert get_neighbour_positions(n, data, ln, x, y) == expected


def test_solve_2():
    assert solve_2(DATA) == 467835
