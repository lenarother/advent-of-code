import pytest

from .solution import solve

EXAMPLES = (
    ('abcdef', 609043),
    ('pqrstuv', 1048970),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
