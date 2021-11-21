import io

import pytest

from .solution import (
    count_valid_triangles,
    is_triangle_valid,
    read_input_vertically,
)

EXAMPLE = [
    ((1, 1, 1), True),
    ((1, 1, 2), False),
    ((1, 2, 1), False),
    ((2, 1, 1), False),
    ((5, 3, 7), True),
    ((2, 2, 1), True),
    ((5, 10, 25), False),
]

COUNT_EXAMPLES = [
    (((1, 1, 1), (1, 1, 2)), 1),
]

INPUT_EXAMPLES = [
    ("""101 301 501
        102 302 502
        103 303 503""", [
        (101, 102, 103),
        (301, 302, 303),
        (501, 502, 503)
     ]),
]


@pytest.mark.parametrize('edges,result', EXAMPLE)
def test_check_triangle(edges, result):
    assert is_triangle_valid(edges) == result


@pytest.mark.parametrize('triangles_list,count', COUNT_EXAMPLES)
def test_count_valid_triangles(triangles_list, count):
    assert count_valid_triangles(triangles_list) == count


@pytest.mark.parametrize('input_data,expected', INPUT_EXAMPLES)
def test_read_input_vertically(input_data, expected):
    input_data = io.StringIO(input_data)
    result = read_input_vertically(input_data)
    assert [i for i in result] == expected
