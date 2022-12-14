from .solution import find_floor, parse_scan, solve, solve2

DATA = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_solve():
    assert solve(DATA) == 24


def test_parse():
    assert len(parse_scan(DATA)) == 20


def test_find_floor():
    scan = parse_scan(DATA)
    assert find_floor(scan) == 11


def test_solve2():
    assert solve2(DATA) == 93
