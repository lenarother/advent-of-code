"""
Data to move:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
"""

from copy import deepcopy

from .solution import make_move2, solve

MOVES = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

DATA = {
    '1': list('ZN'),
    '2': list('MCD'),
    '3': list('P'),
}


def test_solve():
    input_data = deepcopy(DATA)
    assert solve(MOVES, input_data) == 'CMZ'


def test_solve2():
    input_data = deepcopy(DATA)
    assert solve(MOVES, input_data, make_move2) == 'MCD'
