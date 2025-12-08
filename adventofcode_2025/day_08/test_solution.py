import pytest

from .solution import solve, solve2

DATA = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

EXAMPLES = (
    (DATA, 10, 40),
)

EXAMPLES_2 = (
    (DATA, 25272),
)


@pytest.mark.parametrize('data, i, expected', EXAMPLES)
def test_solve(data, i, expected):
    assert solve(data, i) == expected


@pytest.mark.parametrize('data, expected', EXAMPLES_2)
def test_solve_2(data, expected):
    assert solve2(data) == expected
