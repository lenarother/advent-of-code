import pytest

from .solution import solve, solve2

EXAMPLES_1 = (
    ('[1,2,3]', 6),
    ('{"a":2,"b":4}', 6),
    ('[[[3]]]}', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}', 0),
    ('[]', 0),
    ('{}', 0),
)
EXAMPLES_2 = (
    ('[1,2,3]', 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6),
)


@pytest.mark.parametrize('data,expected', EXAMPLES_1)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_2)
def test_solve2(data, expected):
    assert solve2(data) == expected
