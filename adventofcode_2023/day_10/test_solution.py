from .solution import solve, solve_2

DATA_1 = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

DATA_2 = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

DATA_3 = """
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
"""

DATA_4 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


def test_solve():
    assert solve(DATA_1) == 4
    assert solve(DATA_2) == 8


def test_solve_2():
    assert solve_2(DATA_3) == 8
    assert solve_2(DATA_4) == 10
