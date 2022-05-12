import pytest

from .solution import execute, solve

INPUT = """
inc a
jio a, +2
tpl a
inc a
"""


@pytest.mark.parametrize(
    'register_in, code, register_out',
    (
        ({'a': 0, 'b': 0}, 'inc a', {'a': 1, 'b': 0}),
        ({'a': 0, 'b': 0}, 'inc b', {'a': 0, 'b': 1}),

        ({'a': 2, 'b': 0}, 'hlf a', {'a': 1, 'b': 0}),
        ({'a': 0, 'b': 2}, 'hlf b', {'a': 0, 'b': 1}),

        ({'a': 1, 'b': 0}, 'tpl a', {'a': 3, 'b': 0}),
        ({'a': 0, 'b': 1}, 'tpl b', {'a': 0, 'b': 3}),

        ({'a': 0, 'b': 0}, 'inc a\ninc a', {'a': 2, 'b': 0}),

        ({'a': 0, 'b': 0}, 'inc a\ninc a', {'a': 2, 'b': 0}),
        ({'a': 0, 'b': 0}, 'inc a\njmp +1\ninc a', {'a': 2, 'b': 0}),

        ({'a': 1, 'b': 0}, 'inc a\njie a, +2\ninc a', {'a': 2, 'b': 0}),

        ({'a': 0, 'b': 0}, 'inc a\njio a, +2\ninc a', {'a': 1, 'b': 0}),
    )
)
def test_execute(register_in, code, register_out):
    assert execute(register_in, code) == register_out


@pytest.mark.parametrize(
    'register_in, code',
    (
        ({'a': 1, 'b': 0}, 'hlf a'),
    )
)
def test_execute_fails(register_in, code):
    with pytest.raises(ValueError):
        execute(register_in, code)


def test_solve():
    assert solve(INPUT) == {'a': 2, 'b': 0}
