import pytest

from .solution import is_id_valid, is_id_valid_2, solve

DATA = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""  # NoQA


@pytest.mark.parametrize(
    'data, algorithm, expected',
    (
        (DATA, is_id_valid, 1227775554),
        (DATA, is_id_valid_2, 4174379265),
    ),
)
def test_solve(data, algorithm, expected):
    assert solve(data, algorithm) == expected
