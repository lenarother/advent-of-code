import pytest

from .solution import Game

EXAMPLES = (
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_run(data, expected):
    g = Game(data)
    g.solve()
    assert ','.join(list(map(str, g.data))) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert Game(data).solve() == int(expected.split(',')[0])
