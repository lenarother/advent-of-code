import pytest

from .solution import run_monad, run_monad_simplified

EXAMPLE_1 = """
inp x
mul x -1
"""

EXAMPLE_2 = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""

EXAMPLE_3 = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
"""

EXAMPLE_4 = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
"""

EXAMPLES = (
    (EXAMPLE_1, '21111111111111', (0, -2, 0, 0)),
    (EXAMPLE_2, '1', (1, 1, 7, 7)),
    (EXAMPLE_2, '2', (2, 1, 8, 8)),
    (EXAMPLE_2, '3', (3, 1, 9, 9)),
    (EXAMPLE_3, '1', (1, 1, 15, 15)),
    (EXAMPLE_3, '2', (2, 1, 16, 16)),
    (EXAMPLE_3, '3', (3, 1, 17, 17)),
    (EXAMPLE_4, '11', (1, 1, 15, 197)),
)


@pytest.mark.parametrize('data,input_str,expected', EXAMPLES)
def test_run_monad(data, input_str, expected):
    assert run_monad(data, input_str) == expected


def test_run_run_monad_simplified():
    data = open('input_data.txt').read()
    input_string = '11111111111111'
    long = run_monad(data, input_string)
    short = run_monad_simplified(input_string)
    assert long[-1] == short
