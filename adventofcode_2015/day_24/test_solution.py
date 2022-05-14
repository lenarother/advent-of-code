import pytest

from .solution import solve


@pytest.mark.parametrize(
    'data, n_groups, expected',
    (
        ('2\n1\n1\n1\n1\n', 3, 2),
        ('1\n2\n3\n4\n5\n7\n8\n9\n10\n11', 3, 99),
        ('1\n2\n3\n4\n5\n7\n8\n9\n10\n11', 4, 44),
    )
)
def test_solve(data, n_groups, expected):
    assert solve(data, n_groups) == expected
