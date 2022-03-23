import pytest

from .solution import solve

EXAMPLES = (
    (1, 10),  # 1
    (2, 30),  # 1 + 2
    (3, 40),  # 1 + 3
    (4, 50),  # 1 + 2 + 4
    (4, 60),
    (4, 70),
    (6, 80),  # 1 + 2 + 3 + 6
    (6, 90),
    (6, 100),
    (6, 110),
    (6, 120),
    (8, 130),  # 1 + 2 + 4 + 8
    (8, 140),
    (8, 150),
    (12, 280),  # 1 + 2 + 3 + 4 + 6 + 12
    (24, 600),  # 1 + 2 + 3 + 4 + 6 + 8 + 12 + 24
)


@pytest.mark.parametrize('house_n,presents_count', EXAMPLES)
def test_solve(house_n, presents_count):
    assert solve(presents_count) == house_n
