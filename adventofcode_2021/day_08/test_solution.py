import pytest

from .solution import parse_digits, solve, solve2

DATA = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

DATA_SMALL = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
DATA_PARSE = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'

EXAMPLES = (
    (DATA_SMALL, 2),
    (DATA, 26),
)

EXAMPLES_DECODE = (
    (DATA_SMALL, 8394),
    (DATA, 61229),
)

EXAMPLES_PARSE = (
    (DATA_PARSE, {
        'be': '1',
        'abcdefg': '8',
        'bcdefg': '9',
        'acdefg': '6',
        'bceg': '4',
        'cdefg': '5',
        'abdefg': '0',
        'bcdef': '3',
        'abcdf': '2',
        'bde': '7',
    }),
)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_DECODE)
def test_solve2(data, expected):
    assert solve2(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_PARSE)
def test_parse_digits(data, expected):
    assert parse_digits(data) == expected
