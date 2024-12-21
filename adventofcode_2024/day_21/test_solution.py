import pytest

from .solution import solve

DATA = """
029A
980A
179A
456A
379A
"""
EXAMPLES = (
    (DATA, 126384),
    ('029A', 1972),
    ('980A', 58800),
    ('179A', 12172),
    ('456A', 29184),
    ('379A', 24256),  #
)

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected




#<vA<AA>^>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v <<A>>^A<A>AvA<^AA>A<vAAA>^A

#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+


#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+