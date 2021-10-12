import pytest

from .roman_numbers import (
    FORBIDDEN,
    RomanNumbersExceptions,
    arabic2roman,
    roman2arabic,
)

EXAMPLES_FORBIDDEN = FORBIDDEN + ['CIC']

EXAMPLES = (
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('IX', 9),
    ('XV', 15),
    ('XX', 20),
    ('CMXCIX', 999),
    ('MDCCCXCIV', 1894),
    ('XLIX', 49),
)


def test_convert_roman_to_arabic_invalid_input():
    assert roman2arabic('foo') is None


@pytest.mark.parametrize('roman,arabic', EXAMPLES)
def test_roman_to_arabic(roman, arabic):
    assert roman2arabic(roman) == arabic


@pytest.mark.parametrize('roman', EXAMPLES_FORBIDDEN)
def test_forbiden(roman):
    with pytest.raises(RomanNumbersExceptions):
        roman2arabic(roman)


@pytest.mark.parametrize('roman,arabic', EXAMPLES)
def test_convert_arabic_to_roman(roman, arabic):
    assert arabic2roman(arabic) == roman


@pytest.mark.parametrize('arabic', range(1, 100))
def test_round_trip(arabic):
    assert roman2arabic(arabic2roman(arabic)) == arabic
