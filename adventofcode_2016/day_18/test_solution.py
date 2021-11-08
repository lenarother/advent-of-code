import pytest

from .solution import solve, solve_row, solve_triple

EXAMPLES = (
    ("..^^.", 3, 6),
    ('.^^.^.^^^^', 10, 38),
)

EXAMPLES_ROW = (
    ('..^^.', '.^^^^'),
    ('.^^^^', '^^..^'),
)


EXAMPLES_TRIPLES = (
    ('^^.', '^'),
    ('.^^', '^'),
    ('^..', '^'),
    ('..^', '^'),
    ('...', '.'),
    ('.^.', '.'),
    ('^.^', '.'),
    ('^^^', '.'),
)


@pytest.mark.parametrize('triple,expected', EXAMPLES_TRIPLES)
def test_solve_triple(triple, expected):
    x, _, z = triple
    assert solve_triple(x, z) == expected


@pytest.mark.parametrize('triple,expected', EXAMPLES_ROW)
def test_solve_row(triple, expected):
    assert solve_row(triple) == expected


@pytest.mark.parametrize('row,size,expected', EXAMPLES)
def test_solve(row, size, expected):
    assert solve(row, size) == expected
