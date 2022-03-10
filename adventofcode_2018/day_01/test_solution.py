import pytest

from .solution import solve, solve2

DATA = """
+1
-2
+3
+1
"""

DATA2 = """
+7
+7
-2
-7
-4
"""


EXAMPLES = (
    (DATA, 3),
)

EXAMPLES_2 = (
    (DATA2, 14),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
