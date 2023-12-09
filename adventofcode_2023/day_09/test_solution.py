from .solution import Row, solve, solve_2

DATA = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_solve():
    assert solve(DATA) == 114


def test_solve_2():
    assert solve_2(DATA) == 2


class TestRow:

    def test_add_rows(self):
        row = Row(values="0 3 6 9 12 15")
        row.add_rows()
        assert row.rows == [
            [0, 3, 6, 9, 12, 15],
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ]

    def test_extrapolate(self):
        row = Row(values="0 3 6 9 12 15")
        row.add_rows()
        assert row.extrapolate() == 18
