import pytest

from .solution import count_possible_ids, get_lowest_ip, merge

EXAMPLES = (
    ('0-5', 6),
    ('1-5', 0),
    ('0-3', 4),
    ('2-5', 0),
    ("""
0-5
2-7""", 8),
    ("""
0-5
7-8""", 6),
    ("""
5-8
0-2
4-7""", 3),
)

EXAMPLES_MERGE = (
    ([], []),
    ([(0, 5), (2, 7)], [(0, 7)]),
    ([(0, 5), (7, 8)], [(0, 5), (7, 8)]),
    ([(1, 3), (2, 5)], [(1, 5)]),
    ([(1, 3), (2, 5), (4, 7)], [(1, 7)]),
    ([(1, 2), (3, 5)], [(1, 5)]),
    ([(1, 8), (2, 4)], [(1, 8)]),
    ([(1, 3), (2, 5), (6, 8)], [(1, 8)]),
    ([(6, 8), (1, 3), (2, 5)], [(1, 8)]),
    ([(6, 8), (1, 3), (2, 5), (12, 15), (14, 20)], [(1, 8), (12, 20)]),
)

EXAMPLES_COUNT = (
    ('1-5', 9, 5),
    ('1-5', 6, 2),
    ('0-5', 9, 4),
    ('0-5', 19, 14),
    ('0-3', 9, 6),
    ('1-8', 9, 2),
    ("""
0-5
2-7""", 9, 2),
    ("""
2-3
7-8""", 9, 6),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_lowest_ip(data, expected):
    assert get_lowest_ip(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_MERGE)
def test_merge(data, expected):
    assert merge(data) == expected


@pytest.mark.parametrize('data,max_ip,expected', EXAMPLES_COUNT)
def test_count_possible_ids(data, max_ip, expected):
    assert count_possible_ids(data, max_ip) == expected
