import pytest

from .solution import (
    get_pattern_variants,
    join_pattern,
    pattern_repr,
    solve,
    split_pattern,
)

DATA = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""


def test_solve():
    assert solve(DATA, n=2) == 12


@pytest.mark.parametrize(
    'pattern, variants',
    (
        ('ABC/DEF/GHI', {
            'ABCDEFGHI',
            'GDAHEBIFC',
            'IHGFEDCBA',
            'CFIBEHADG',
            'CBAFEDIHG',
            'ADGBEHCFI',
            'GHIDEFABC',
            'IFCHEBGDA',
        }),
        ('AB/CD', {
            'ABCD',
            'CADB',
            'DCBA',
            'BDAC',
            'BADC',
            'ACBD',
            'CDAB',
            'DBCA',
        }),
    )
)
def test_get_pattern_variants(pattern, variants):
    assert get_pattern_variants(pattern) == variants


@pytest.mark.parametrize(
    'pattern, representation',
    (
        ('ABC/DEF/GHI', 'ABC\nDEF\nGHI'),
        ('ABCDEFGHI', 'ABC\nDEF\nGHI'),
    )
)
def test_pattern_repr(pattern, representation):
    assert pattern_repr(pattern) == representation


@pytest.mark.parametrize(
    'pattern, result_patterns',
    (
        ('ABCD/EFGH/IJKL/MNOP', ['ABEF', 'CDGH', 'IJMN', 'KLOP']),
        (
            'ABCDEF/GHIJKL/MNOPQR/STUVWX/YZabcd/efghij',
            ['ABGH', 'CDIJ', 'EFKL', 'MNST', 'OPUV', 'QRWX', 'YZef', 'abgh', 'cdij']  # noqa
        ),
        ('ABC/DEF/GHI', ['ABCDEFGHI']),
    )
)
def test_pattern_divided_into_sub_patterns(
        pattern, result_patterns
):
    assert split_pattern(pattern) == result_patterns


@pytest.mark.parametrize(
    'fragments, pattern',
    (
        (['ABEF', 'CDGH', 'IJMN', 'KLOP'], 'ABCDEFGHIJKLMNOP'),
        (
            ['ABGH', 'CDIJ', 'EFKL', 'MNST', 'OPUV', 'QRWX', 'YZef', 'abgh', 'cdij'],  # noqa
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij'
        ),
    )
)
def test_join_fragments_into_pattern(
        fragments, pattern
):
    assert join_pattern(fragments) == pattern
