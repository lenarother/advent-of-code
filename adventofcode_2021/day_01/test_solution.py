import pytest

from .solution import solve

EXAMPLES = (
    ([199, 200], 1, 1),
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 1, 7),
    ([199, 200, 208, 210], 3, 1),
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 3, 5),

)


@pytest.mark.parametrize('data,window,expected', EXAMPLES)
def test_solve(data, window, expected):
    assert solve(data, window) == expected
