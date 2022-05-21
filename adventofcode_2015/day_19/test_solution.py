import pytest

from .solution import (
    molecule_reverse_generator,
    parse,
    parse_instructions_reverse,
    solve,
    solve_fragment,
)

DATA1 = """
e => H
e => O
H => HO
H => OH
O => HH

HOH
"""

DATA2 = """
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA1, 4),
        (DATA2, 7),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA1, 3),
        (DATA2, 6),
    )
)
def test_solve2(data, expected):
    molecule, instructions = parse(data, parse_instructions_reverse)
    result = solve_fragment(replacements=instructions, molecule=molecule)
    assert result == expected


@pytest.mark.parametrize(
    'molecule, replacements, expected',
    (
        ('axbxa', {'b': 'B'}, {'axBxa'}),
        ('axbxa', {'a': 'A'}, {'Axbxa', 'axbxA'}),
        ('axbxa', {'a': 'A', 'b': 'B'}, {'axBxa', 'Axbxa', 'axbxA'}),
    )
)
def test_molecule_reverse_generator(molecule, replacements, expected):
    assert set(molecule_reverse_generator(molecule, replacements)) == expected
