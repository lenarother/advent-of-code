import pytest

from .solution import distance_generator, get_n_winning_times


@pytest.mark.parametrize(
    "t, expected",
    (
        (7, [0, 6, 10, 12, 12, 10, 6, 0]),
    )
)
def test_distance_generator(t, expected):
    assert list(distance_generator(t)) == expected


@pytest.mark.parametrize(
    "t, dist, expected",
    (
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
        (71530, 940200, 71503)
    )
)
def test_get_n_winning_times(t, dist, expected):
    assert get_n_winning_times(t, dist) == expected
