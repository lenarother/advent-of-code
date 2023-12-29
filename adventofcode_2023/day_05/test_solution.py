import pytest

from .solution import convert_single_range, solve, solve_2

DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_solve():
    assert solve(DATA) == 35


def test_solve_2():
    assert solve_2(DATA) == 46


@pytest.mark.parametrize(
    'input_range, source_range, destination_range, expected_new_input, expected_result',  # noqa
    (
        # C  AB  D
        (range(5, 8), range(1, 10), range(21, 30), [], [range(25, 28)]),  # noqa
        # C  A  D  B
        (range(5, 20), range(1, 10), range(21, 30), [range(10, 20)], [range(25, 30)]),  # noqa
        # AB CD
        (range(5, 20), range(30, 40), range(20, 30), [range(5, 20)], []),  # noqa
        # A  CD  B
        (range(20, 40), range(30, 35), range(130, 135), [range(20, 30), range(35, 40)], [range(130, 135)]),  # noqa
        # A  C  B  D
        (range(20, 40), range(30, 45), range(130, 145), [range(20, 30)], [range(130, 140)]),  # noqa
    )
)
def test_convert_single_range(
        input_range,
        source_range,
        destination_range,
        expected_new_input,
        expected_result
):
    new_input, result = convert_single_range(
        input_range, source_range, destination_range
    )
    assert new_input == expected_new_input
    assert result == expected_result
