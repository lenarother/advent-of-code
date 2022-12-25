import pytest

from .solution import execute, execute2, solve, solve2

DATA = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

DATA_2 = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""


def test_solve():
    assert solve(DATA) == 4


def test_solve2():
    assert solve2(DATA_2) == 3


@pytest.mark.parametrize(
    'instructions, register, sounds',
    (
        ('set a 1', {'a': 1}, {}),
        ('set a 0', {'a': 0}, {}),
        ('set a -1', {'a': -1}, {}),
        ('set a 2\nset a 5', {'a': 5}, {}),
        ('set b 2\nset a b', {'a': 2, 'b': 2}, {}),

        ('add a 2', {'a': 2}, {}),
        ('set a 2\nadd a 5', {'a': 7}, {}),
        ('set a 2\nadd a -5', {'a': -3}, {}),
        ('set b 2\nadd a b', {'a': 2, 'b': 2}, {}),

        ('mul a 10', {'a': 0}, {}),
        ('set a 2\nmul a 10', {'a': 20}, {}),
        ('set a 2\nset b 2\nmul a b', {'a': 4, 'b': 2}, {}),
        ('set a 2\nset b -2\nmul a b', {'a': -4, 'b': -2}, {}),

        ('set a 10\nmod a 5', {'a': 0}, {}),
        ('set a 10\nset b 3\nmod a b', {'a': 1, 'b': 3}, {}),

        ('snd a', {}, {'a': 0}),
        ('set a 10\nsnd a', {'a': 10}, {'a': 10}),

        ('rcv a', {}, {}),
        ('set a 10\nsnd a\nset a 5\nrcv a', {'a': 10}, {'a': 10}),
        ('set a 10\nsnd a\nset a 0\nrcv a', {'a': 0}, {'a': 10}),
        ('set a 10\nset a 5\nrcv a', {'a': 5}, {}),

        ('jgz a 5', {}, {}),
        ('set a 1\njgz a 2\nset a 3', {'a': 1}, {}),
        ('set a 0\njgz a 2\nset a 3', {'a': 3}, {}),
        ('set a -1\njgz a 2\nset a 3', {'a': 3}, {}),

    )
)
def test_execute(
        instructions,
        register,
        sounds
):
    result_register, result_sounds, _ = execute(instructions)
    assert result_register == register
    assert result_sounds == sounds


@pytest.mark.parametrize(
    'instructions, p0_expected, p1_expected',
    (
        ('set a 1', ({'p': 0, 'a': 1}, [], []), ({'a': 1, 'p': 1}, [], [])),
        ('set a 10\nsnd a\nsnd p', ({'p': 0, 'a': 10}, [10, 0], [10, 1]), ({'a': 10, 'p': 1}, [10, 1], [10, 0])),
        (DATA_2, ({'p': 0, 'a': 0, 'b': 0, 'c': 1}, [], []), ({'p': 1, 'a': 0, 'b': 0, 'c': 0}, [], [])),
    )
)
def test_execute2(
        instructions,
        p0_expected,
        p1_expected
):
    p0_register, p0_sent, p0_received = p0_expected
    p1_register, p1_sent, p1_received = p1_expected
    p0, p1 = execute2(instructions)

    assert p0.register == p0_register
    assert list(p0.send_mq) == p0_sent
    assert list(p0.receive_mq) == p0_received

    assert p1.register == p1_register
    assert list(p1.send_mq) == p1_sent
    assert list(p1.receive_mq) == p1_received

    assert list(p0.send_mq) == list(p1.receive_mq)
    assert list(p1.send_mq) == list(p0.receive_mq)

