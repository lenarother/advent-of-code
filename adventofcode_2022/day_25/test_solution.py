import pytest

from .solution import decimal_to_snafu, snafu_to_decimal, solve

DATA = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""

SNAFU_DECIMAL = [
    ('1', 1),
    ('2', 2),
    ('1=', 3),
    ('1-', 4),
    ('10', 5),
    ('11', 6),
    ('12', 7),
    # ('2=', 8),
    # ('2-', 9),
    ('20', 10),
    ('1=0', 15),
    ('1-0', 20),
    # ('2=-01', 976),
    # ('1=11-2', 2022),
    # ('2=-1=0', 4890),
    # ('1-0---0', 12345),
    # ('1121-1110-1=0', 314159265),
]

#
# @pytest.mark.parametrize('snafu, decimal', SNAFU_DECIMAL)
# def test_snafu_to_decimal(snafu, decimal):
#     assert snafu_to_decimal(snafu) == decimal


@pytest.mark.parametrize('snafu, decimal', SNAFU_DECIMAL)
def test_decimal_to_snafu(snafu, decimal):
    assert decimal_to_snafu(decimal) == snafu

# def test_solve():
#     assert solve(DATA) == 4890