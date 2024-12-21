import pytest

from .solution import solve

DATA = """
029A
980A
179A
456A
379A
"""

EXAMPLES = (
    (DATA, 126384),
    ('029A', 1972),
    ('980A', 58800),
    ('179A', 12172),
    ('456A', 29184),
    ('379A', 24256),  #
)

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
