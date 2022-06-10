import pytest

from .solution import execute, is_prime


@pytest.mark.parametrize(
    'instructions, register, multiplication_count',
    (
        ('set a 1', {'a': 1}, 0),
        ('set a 0', {'a': 0}, 0),
        ('set a -1', {'a': -1}, 0),
        ('set a 2\nset a 5', {'a': 5}, 0),
        ('set b 2\nset a b', {'a': 2, 'b': 2}, 0),

        ('mul a 10', {'a': 0}, 1),
        ('set a 2\nmul a 10', {'a': 20}, 1),
        ('set a 2\nset b 2\nmul a b', {'a': 4, 'b': 2}, 1),
        ('set a 2\nset b -2\nmul a b', {'a': -4, 'b': -2}, 1),

        ('jnz a 5', {}, 0),
        ('set a 1\njnz a 2\nset a 3', {'a': 1}, 0),
        ('set a 0\njnz a 2\nset a 3', {'a': 3}, 0),
        ('set a -1\njnz a 2\nset a 3', {'a': -1}, 0),

        ('sub a 5', {'a': -5}, 0),
        ('sub a -5', {'a': 5}, 0),
    )
)
def test_execute(
        instructions,
        register,
        multiplication_count
):
    result_register, mc = execute(instructions)
    assert result_register == register
    assert mc == multiplication_count


@pytest.mark.parametrize(
    'n, expected',
    (
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (19, True),
        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (10, False),
        (12, False),
        (14, False),
        (15, False),
        (16, False),
        (18, False),
        (20, False),
        (200, False),
        (2000, False),
    )
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected
