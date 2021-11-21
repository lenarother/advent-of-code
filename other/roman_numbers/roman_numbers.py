"""Convert a roman number into an arabic number"""

ROMAN = list('MDCLXVI')
ARABIC = [1000, 500, 100, 50, 10, 5, 1]

ROMAN_SUB = 'IV,IX,XL,XC,CD,CM'.split(',')
ARABIC_SUB = [4, 9, 40, 90, 400, 900]

ROMAN_NUMBERS = dict(zip(ROMAN, ARABIC))
ARABIC_NUMBERS = dict(zip(ARABIC + ARABIC_SUB, ROMAN + ROMAN_SUB))

FORBIDDEN = ['IL', 'IC', 'VC', 'VD', 'XM', 'IM']


class RomanNumbersExceptions(Exception):
    pass


def get_value(i):
    return ROMAN_NUMBERS.get(i, 0)


def get_real_value(value, previous):
    return value if value >= previous else -value


def validate_roman(roman):
    for i in FORBIDDEN:
        if i in roman:
            raise RomanNumbersExceptions('Invalid roman number')


def roman2arabic(roman):
    validate_roman(roman)
    result = 0
    previous = 0
    for i in roman[::-1]:
        value = get_value(i)
        result += get_real_value(value, previous)
        previous = value
    return result or None


def arabic2roman(arabic):
    for i in sorted(ARABIC_NUMBERS, reverse=True):
        if arabic >= i:
            return ARABIC_NUMBERS.get(i) + arabic2roman(arabic - i)
    return arabic * 'I'
