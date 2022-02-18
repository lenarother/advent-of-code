from .solution import find_combinations_count, find_min_combinations_count


def test_find_combinations_count():
    assert find_combinations_count([20, 15, 10, 5, 5], 25) == 4


def test_find_min_combinations_count():
    assert find_min_combinations_count([20, 15, 10, 5, 5], 25) == 3
