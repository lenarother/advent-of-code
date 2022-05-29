import pytest

from .solution import (
    base_generator,
    create_compare_gen,
    hex_16_generator,
    hex_generator,
    solve,
)


@pytest.mark.parametrize(
    'start_number, factor, i, expected',
    (
        # Generator A
        (65, 16807, 1, 1092455),
        (65, 16807, 2, 1181022009),
        (65, 16807, 3, 245556042),
        (65, 16807, 4, 1744312007),
        (65, 16807, 5, 1352636452),

        # Generator B
        (8921, 48271, 1, 430625591),
        (8921, 48271, 2, 1233683848),
        (8921, 48271, 3, 1431495498),
        (8921, 48271, 4, 137874439),
        (8921, 48271, 5, 285222916),
    )
)
def test_generator(start_number, i, factor, expected):
    g = base_generator(start_number, factor)
    while i:
        n = next(g)
        i -= 1
    assert n == expected


@pytest.mark.parametrize(
    'start_number, factor, i, expected',
    (
        # Generator A
        (65, 16807, 1, '00000000000100001010101101100111'),
        (65, 16807, 2, '01000110011001001111011100111001'),
        (65, 16807, 3, '00001110101000101110001101001010'),
        (65, 16807, 4, '01100111111110000001011011000111'),
        (65, 16807, 5, '01010000100111111001100000100100'),
        #
        # # Generator B
        (8921, 48271, 1, '00011001101010101101001100110111'),
        (8921, 48271, 2, '01001001100010001000010110001000'),
        (8921, 48271, 3, '01010101010100101110001101001010'),
        (8921, 48271, 4, '00001000001101111100110000000111'),
        (8921, 48271, 5, '00010001000000000010100000000100'),
    )
)
def test_hex_generator(start_number, i, factor, expected):
    gen = base_generator(start_number, factor)
    g = hex_generator(gen)
    while i:
        n = next(g)
        i -= 1
    assert n == expected


@pytest.mark.parametrize(
    'start_number, factor, i, expected',
    (
        # Generator A
        (65, 16807, 1, '1010101101100111'),
        (65, 16807, 2, '1111011100111001'),
        (65, 16807, 3, '1110001101001010'),
        (65, 16807, 4, '0001011011000111'),
        (65, 16807, 5, '1001100000100100'),
        #
        # # Generator B
        (8921, 48271, 1, '1101001100110111'),
        (8921, 48271, 2, '1000010110001000'),
        (8921, 48271, 3, '1110001101001010'),
        (8921, 48271, 4, '1100110000000111'),
        (8921, 48271, 5, '0010100000000100'),
    )
)
def test_hex_16_generator(start_number, i, factor, expected):
    base_gen = base_generator(start_number, factor)
    hex_gen = hex_generator(base_gen)
    g = hex_16_generator(hex_gen)
    while i:
        n = next(g)
        i -= 1
    assert n == expected


@pytest.mark.parametrize(
    'start_number_a, start_number_b, i, expected',
    (
        (65, 8921, 1, 0),
        (65, 8921, 5, 1),
    )
)
def test_compare_generators(
        start_number_a,
        start_number_b,
        i,
        expected
):
    cg = create_compare_gen(start_number_a, start_number_b)
    count = 0
    while i:
        count += next(cg)
        i -= 1
    assert count == expected


@pytest.mark.slow
def test_solve():
    assert solve(65, 8921, 40_000_000) == 588


@pytest.mark.slow
def test_solve2():
    assert solve(65, 8921, 5_000_000, 4, 8) == 309
