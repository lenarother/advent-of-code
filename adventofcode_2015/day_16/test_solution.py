import pytest

from .solution import solve

DATA = """
Sue 1: perfumes: 2, cars: 8, trees: 9
Sue 10: trees: 7, perfumes: 2, akitas: 5
Sue 20: children: 3, goldfish: 5, vizslas: 0"""

EXAMPLES = (
    (DATA, '20'),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
