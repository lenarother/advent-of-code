import pytest

from .bathroom_code import KEYPAD_DIAMOND, find_code

INSTRUCTIONS = (
    ('R', '6'),
    ('L', '4'),
    ('U', '2'),
    ('D', '8'),
    ('UL', '1'),
    ('UUUR', '3'),
    ('LLUURRRDDDLLLUR', '5'),  # roundtrip
    ("""
ULL
RRDDD
LURDL
UUUUD""", '1985'
     ),
)

INSTRUCTIONS_DIAMOND = (
    ('LUDRULURULRUDRURDRURDLDRDLDRLDULLDUL', '5'),  # roundtrip
    ("""
ULL
RRDDD
LURDL
UUUUD""", '5DB3'),
)


@pytest.mark.parametrize('instructions,code', INSTRUCTIONS)
def test_find_code(instructions, code):
    assert find_code(instructions) == code


@pytest.mark.parametrize('instructions,code', INSTRUCTIONS_DIAMOND)
def test_find_code_diamond(instructions, code):
    assert find_code(instructions, KEYPAD_DIAMOND) == code
