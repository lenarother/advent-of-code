import pytest

from .solution import dance


@pytest.mark.parametrize(
    'seq, moves,expected',
    (
        ('abcde', '', 'abcde'),
        ('abcde', 's1', 'eabcd'),
        ('abcde', 's3', 'cdeab'),
        ('eabcd', 'x3/4', 'eabdc'),
        ('eabdc', 'pe/b', 'baedc'),
        ('abcde', 's1,x3/4,pe/b', 'baedc'),
    )
)
def test_dance(seq, moves, expected):
    assert dance(seq, moves) == expected
