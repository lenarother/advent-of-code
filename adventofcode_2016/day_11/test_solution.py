import pytest

from .solution import parse, solve

EXAMPLES = (
    ("""
F4 .  HG .  .  .  
F3 E  .  .  HM .  
F2 .  .  .  .  .  
F1 .  .  .  .  . """, 1),
    ("""
F4 .  HG .  .  .
F3 .  .  .  .  .
F2 .  .  .  .  .
F1 E  .  .  HM . """, 3),
    ("""
F4 .  HG .  .  .
F3 .  .  .  .  .
F2 E  .  .  HM .
F1 .  .  .  .  . """, 2),
    ("""
F4 .  .  .  .  .
F3 .  .  .  .  .
F2 E  .  .  HM .
F1 .  HG .  .  . """, 4),
    ("""
F4 E  .  .  HM .
F3 .  .  .  .  .
F2 .  .  .  .  .
F1 .  HG .  .  . """, 6),
    ("""
F4 .  .  .  .  .
F3 E  HG .  .  .
F2 .  .  .  .  .
F1 .  .  .  HM . """, 5),
    ("""
F4 .  .  .  .  LM
F3 E  HG .  .  .
F2 .  .  LG .  .
F1 .  .  .  HM . """, 9),
    ("""
F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM """, 11),
)

EXAMPLES_PARSE_ELEVATOR = (
    ("""
F4 .  HG .  .  .  
F3 E  .  .  HM .  
F2 .  .  .  .  .  
F1 .  .  .  .  . """, 3),
)

EXAMPLES_PARSE_FLOORS = (
    ("""
F4 .  HG .  .  .  
F3 E  .  .  HM .  
F2 .  .  .  .  .  
F1 .  .  .  .  . """, [(1, 0), (2, 0), (3, 1), (4, 1)]),
    ("""
F4 .  .  .  .  .  
F3 .  .  .  LG .  
F2 .  HG .  .  .  
F1 E  .  HM .  LM """, [(1, 2), (2, 1), (3, 1), (4, 0)]),
)

EXAMPLES_VALIDATION = (
    ("""
F4 .  HG .  .  .  
F3 E  .  .  HM .  
F2 .  .  .  .  .  
F1 .  .  .  .  . """, {1: True, 2: True, 3: True, 4:True}),
    ("""
F4 .  .  .  .  .  
F3 .  .  .  LG .  
F2 .  HG .  .  LM  
F1 E  .  HM .  .  """, {1: True, 2: False, 3: True, 4:True}),
    ("""
F4 .  .  .  .  .  
F3 .  HG  .  LG .  
F2 .  .  .  .  LM  
F1 E  .  HM .  .  """, {1: True, 2: True, 3: True, 4:True}),
    ("""
F4 .  .  .  .  .  
F3 .  HG HM .  LM   
F2 .  .  .  .  .  
F1 E  .  .  LG .  """, {1: True, 2: True, 3: False, 4:True}),
)

EXAMPLES_REPR = (
    ("""
F4 .  HG .  .  .  
F3 E  .  .  HM .  
F2 .  .  .  .  .  
F1 .  .  .  .  . """, '<Building E3 <F1 >, <F2 >, <F3 HM>, <F4 HG>>'),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,elevator', EXAMPLES_PARSE_ELEVATOR)
def test_parse_elevator(data, elevator):
    building = parse(data)
    assert building.elevator == elevator


@pytest.mark.parametrize('data,floors', EXAMPLES_PARSE_FLOORS)
def test_parse_floors(data, floors):
    building = parse(data)
    for f, items_count in floors:
        assert len(building.floors[f].items) == items_count


@pytest.mark.parametrize('data,valid', EXAMPLES_VALIDATION)
def test_validate_floor(data, valid):
    building = parse(data)
    for k, v in valid.items():
        assert building.floors[k].is_valid() == v


@pytest.mark.parametrize('data,repr', EXAMPLES_REPR)
def test_building_repr(data, repr):
    building = parse(data)
    assert str(building) == repr
