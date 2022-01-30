import pytest

from .solution import solve

DATA = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

EXAMPLES = (
    (DATA, min, 605),
    (DATA, max, 982),
)


@pytest.mark.parametrize('data,f,expected', EXAMPLES)
def test_solve(data, f, expected):
    assert solve(data, f) == expected
