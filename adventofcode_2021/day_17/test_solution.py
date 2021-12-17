import pytest

from .solution import (
    get_trajectory,
    in_target,
    may_reach_target,
    parse_area,
    solve,
    solve2,
    step,
)

DATA = 'target area: x=20..30, y=-10..-5'

EXAMPLES_POSITIONS = (
    ((6, 3), 1, ((6, 3),)),
    ((6, 3), 2, ((6, 3), (11, 5))),
    ((6, 3), 3, ((6, 3), (11, 5), (15, 6))),
    ((6, 3), 4, ((6, 3), (11, 5), (15, 6), (18, 6))),
)

EXAMPLES_MAY_REACH_TARGET = (
    (DATA, (7, 2), True),
    (DATA, (6, 3), True),
    (DATA, (9, 0), True),
)

EXAMPLES_IN_TARGET = (
    (DATA, (28, -7), True),
)

EXAMPLES_AREA = (
    (DATA, [20, 30, -10, -5]),
)

EXAMPLES_TRAJECTORY = (
    (DATA, (17, -4), None),
    (
        DATA, (6, 3), [(6, 3), (11, 5), (15, 6), (18, 6), (20, 5), (21, 3), (21, 0), (21, -4), (21, -9)]),  # noqa
)

EXAMPLES_Y = (
    (DATA, 45),
)

EXAMPLES_ALL = (
    (DATA, 112),
)


@pytest.mark.parametrize('pos,steps,expected', EXAMPLES_POSITIONS)
def test_step_generator(pos, steps, expected):
    assert tuple([step(pos) for i in range(steps)])


@pytest.mark.parametrize('data,pos,expected', EXAMPLES_IN_TARGET)
def test_in_target(data, pos, expected):
    target = parse_area(data)
    assert in_target(pos, target) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_AREA)
def test_parse_area(data, expected):
    assert parse_area(data) == expected


@pytest.mark.parametrize('data,pos,expected', EXAMPLES_MAY_REACH_TARGET)
def test_may_reach_target(data, pos, expected):
    target = parse_area(data)
    assert may_reach_target(pos, target) == expected


@pytest.mark.parametrize('data,velocity,expected', EXAMPLES_TRAJECTORY)
def test_get_trajectory(data, velocity, expected):
    target = parse_area(data)
    assert get_trajectory(velocity, target) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_Y)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_ALL)
def test_solve2(data, expected):
    assert solve2(data) == expected
