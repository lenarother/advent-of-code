import pytest

from .find_distance import walk, walk_until_visited

EXAMPLES = (
    ('R1', 1),
    ('R2', 2),
    ('R1, R2', 3),
    ('L1', 1),
    ('R2, L3', 5),
    ('R2, R2, R2', 2),
    ('R2, R2, R2, R2', 0),
    ('R2, R2, R2, R2, R2', 2),
    ('R2, R2, R2, R2, R2, R2', 4),
    ('R2, R2, R2, R2, R2, R2, R2', 2),
    ('R2, R2, R2, R2, R2, R2, R2, R2', 0),
    ('R1, L1, L1', 1),
    ('R1, L1, R1', 3),
    ('R5, L5, R5, R3', 12),
    ('R10', 10),
)

EXAMPLES_UNTIL_VISITED = (
    ('R8, R4, R4, R8', 4),
    ('R5, L1, L1, L1, R8', 4),
    ('R5, L1, L1, R1, L1, L8', 3),
)


@pytest.mark.parametrize('path,distance', EXAMPLES)
def test_walk(path, distance):
    assert walk(path) == distance


@pytest.mark.parametrize('path,distance', EXAMPLES_UNTIL_VISITED)
def test_walk_until_visited(path, distance):
    assert walk_until_visited(path) == distance
