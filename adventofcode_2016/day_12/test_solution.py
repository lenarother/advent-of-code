import pytest

from .solution import solve


EXAMPLES = (
    ("""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""", (42, 0, 0, 0)),
    ('cpy 41 a', (41, 0, 0, 0)),
    ('cpy 42 a', (42, 0, 0, 0)),
    ('cpy 1 b', (0, 1, 0, 0)),
    ('cpy -1 b', (0, -1, 0, 0)),
    ("""cpy 7 b
cpy 8 c""", (0, 7, 8, 0)),
    ("""cpy 7 b
cpy b d""", (0, 7, 0, 7)),
    ('inc a', (1, 0, 0, 0)),
    ("""inc b
inc b
inc c""", (0, 2, 1, 0)),
    ('dec a', (-1, 0, 0, 0)),
    ("""dec b
dec b
dec c""", (0, -2, -1, 0)),
    ("""inc a
cpy a b""", (1, 1, 0, 0)),
    ("""cpy 1 a
jnz a 2
dec a
inc a""", (2, 0, 0, 0)),
    ("""cpy 5 a
dec a 
jnz a -1""", (0, 0, 0, 0)),
    ("""jnz 1 8""", (0, 0, 0, 0)),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected
