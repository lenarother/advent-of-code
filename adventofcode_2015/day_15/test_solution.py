from .solution import parse, solve

DATA = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def test_parse():
    assert parse(DATA) == [(-1, -2, 6, 3, 8), (2, 3, -2, -1, 3)]


def test_solve():
    assert solve(DATA) == 62842880
    assert solve(DATA, calories=True) == 57600000
