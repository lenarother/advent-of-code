import pytest

from .solution import (
    StepQueue,
    find_root_dependencies,
    parse_data,
    solve,
    solve2,
)

DATA_7 = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""

DATA_1 = """
Step F must be finished before step E can begin.
"""

DATA_CIRCLE = """
Step A must be finished before step A can begin.
"""


@pytest.mark.parametrize(
    "data, expected",
    (
        (DATA_1, {'E': ['F']}),
        (DATA_7, {
            # step requires other steps
            'A': ['C'],
            'B': ['A'],
            'D': ['A'],
            'E': ['B', 'D', 'F'],
            'F': ['C'],
        }),
    )
)
def test_parse(data, expected):
    dependencies_dict = parse_data(data)
    assert expected == dependencies_dict


@pytest.mark.parametrize(
    "data, expected",
    (
        (DATA_1, ['F']),
        (DATA_7, ['C']),
    )
)
def test_find_root_elements(data, expected):
    dependencies_dict = parse_data(data)
    assert set(expected) == find_root_dependencies(dependencies_dict)


@pytest.mark.parametrize(
    'data, expected',
    (
        (DATA_1, 'FE'),
        (DATA_7, 'CABDFE'),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


# Part 2


@pytest.mark.parametrize(
    "data, expected",
    (
        (DATA_1, {'E': ['F']}),
        (DATA_7, {
            # step requires other steps
            'A': ['C'],
            'B': ['A'],
            'D': ['A'],
            'E': ['B', 'D', 'F'],
            'F': ['C'],
        }),
    )
)
def test_parse_data(data, expected):
    step_queue = StepQueue(data)
    assert expected == step_queue.dependency_dict


@pytest.mark.parametrize(
    "data, expected",
    (
        (DATA_1, ['F']),
        (DATA_7, ['C']),
    )
)
def test_find_available_elements(data, expected):
    step_queue = StepQueue(data)
    result = set()
    while not step_queue.todo.empty():
        result.add(step_queue.todo.get())
    assert set(expected) == result


def test_solve2():
    assert solve2(DATA_7, 2, 0) == 15
