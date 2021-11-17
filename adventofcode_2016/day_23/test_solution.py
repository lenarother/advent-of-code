import pytest

from .solution import parse, solve

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
    ("""cpy 5 a
tgl 1
inc a""", (4, 0, 0, 0)),
    ("""cpy 5 a
tgl 8
inc a""", (6, 0, 0, 0)),
    ('tgl 0', (0, 0, 0, 0)),
    ("""cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""", (3, 0, 0, 0)),
    ("""cpy 5 a
cpy -1 b
dec a
jnz a b""", (0, -1, 0, 0)),
)

EXAMPLES_PARSE = (
    ('cpy 41 a', {0: {'name': 'cpy', 'values': (41, 'a')}}),
    ('cpy b a', {0: {'name': 'cpy', 'values': ('b', 'a')}}),
    ('cpy -41 a', {0: {'name': 'cpy', 'values': (-41, 'a')}}),
    ('inc a', {0: {'name': 'inc', 'values': ('a',)}}),
    ('dec b', {0: {'name': 'dec', 'values': ('b',)}}),
    ('jnz 1 8', {0: {'name': 'jnz', 'values': (1, 8)}}),
    ('jnz c -2', {0: {'name': 'jnz', 'values': ('c', -2)}}),
    ('jnz c a', {0: {'name': 'jnz', 'values': ('c', 'a')}}),
    ('tgl -2', {0: {'name': 'tgl', 'values': (-2,)}}),
    ('tgl c', {0: {'name': 'tgl', 'values': ('c',)}}),
    ("""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""", {
        0: {'name': 'cpy', 'values': (41, 'a')},
        1: {'name': 'inc', 'values': ('a',)},
        2: {'name': 'inc', 'values': ('a',)},
        3: {'name': 'dec', 'values': ('a',)},
        4: {'name': 'jnz', 'values': ('a', 2)},
        5: {'name': 'dec', 'values': ('a',)},
    }),
    ("""cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""", {
        0: {'name': 'cpy', 'values': (2, 'a')},
        1: {'name': 'tgl', 'values': ('a',)},
        2: {'name': 'tgl', 'values': ('a',)},
        3: {'name': 'tgl', 'values': ('a',)},
        4: {'name': 'cpy', 'values': (1, 'a')},
        5: {'name': 'dec', 'values': ('a',)},
        6: {'name': 'dec', 'values': ('a',)},
    }),
)

EXAMPLES_MULTIPLY = (
    ("""cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2""", 12, (11, 11, 0, 12)),
)


@pytest.mark.parametrize('data,expected', EXAMPLES_PARSE)
def test_parse(data, expected):
    assert parse(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,a,expected', EXAMPLES_MULTIPLY)
def test_solve_multiply(data, a, expected):
    assert solve(data, a) == expected
