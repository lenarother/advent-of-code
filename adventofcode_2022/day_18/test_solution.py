import pytest

from .solution import solve, get_coord

DATA_1 = """
1,1,1
2,1,1
"""

DATA_2 = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

@pytest.mark.parametrize(
    'x, y, z, expected',
    (
        (0, 0, 0, [
            (1, 1, 1),
            (0, 0, 0),
            (0, 0, 1),
            (1, 0, 0),
            (0, 1, 0),
            (1, 0, 1),
            (1, 1, 0),
            (0, 1, 1)
        ]),
    )

)
def test_get_coord(x, y, z, expected):
    assert get_coord(x, y, z) == set(expected)


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA_1, 10),
        (DATA_2, 64),
    ),
)
def test_solve(data, expected):
    assert solve(data) == expected

#
# @pytest.mark.parametrize(
#     'data, expected',
#     (
#         (DATA_1, 10),
#         (DATA_2, 58),
#     ),
# )
# def test_solve2(data, expected):
#     assert solve3(data) == expected