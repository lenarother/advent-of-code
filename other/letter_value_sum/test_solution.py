import pytest

from .solution import letter_sum

EXAMPLES = (
    ('', 0),
    ('a', 1),
    ('z', 26),
    ('cab', 6),
    ('excellent', 100),
    ('microspectrophotometries', 317),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_letter_sum(data, expected):
    assert letter_sum(data) == expected
