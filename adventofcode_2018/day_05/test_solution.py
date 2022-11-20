import pytest

from .solution import (
    Unit,
    get_polymer_length,
    get_polymer_sequence,
    modified_molecules_generator,
    parse_polymer,
    solve,
    solve2,
)


@pytest.mark.parametrize(
    'data, expected',
    (
        ('aA', Unit('a')),
        ('AA', Unit('A')),
    ),
)
def test_parse_polymer(data, expected):
    assert expected == parse_polymer(data)


@pytest.mark.parametrize(
    'data, expected',
    (
        ('aA', True),
        ('AA', False),
        ('aa', False),
        ('aB', False),
    ),
)
def test_can_remove_unit(data, expected):
    unit = parse_polymer(data)
    assert expected == unit.can_remove()


@pytest.mark.parametrize(
    'data, expected',
    (
        ('a', 1),
        ('Aa', 2),
        ('aaB', 3),
        ('aBcdef', 6),
    ),
)
def test_get_polymer_length(data, expected):
    unit = parse_polymer(data)
    assert expected == get_polymer_length(unit)


@pytest.mark.parametrize(
    'sequence', ('a', 'Aa', 'aaB', 'aBcdef'),
)
def test_get_polymer_sequence(sequence):
    unit = parse_polymer(sequence)
    assert sequence == get_polymer_sequence(unit)


@pytest.mark.parametrize(
    'data, expected',
    (
        ('a', 1),
        ('aA', 0),
        ('aa', 2),
        ('abBA', 0),
        ('dabAcCaCBAcCcaDA', 10),
        ('abcaA', 3),
    ),
)
def test_solve(data, expected):
    assert expected == solve(data)


def test_modified_molecules_generator():
    assert {
        'dbcCCBcCcD',
        'daAcCaCAcCcaDA',
        'dabAaBAaDA',
        'abAcCaCBAcCcaA',
    } == set(modified_molecules_generator('dabAcCaCBAcCcaDA'))


def test_solve2():
    assert 4 == solve2('dabAcCaCBAcCcaDA')
