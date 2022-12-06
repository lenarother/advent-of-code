import pytest

from .solution import solve


@pytest.mark.parametrize(
    'data, n, expected',
    (
        # Part 1
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4, 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 4, 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 4, 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4, 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4, 11),

        # Part 2
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 14, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 14, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14, 26),
    )
)
def test_solve(data, n, expected):
    assert solve(data, n) == expected
