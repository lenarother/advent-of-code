import pytest

from .solution import count_in_memory_chars, count_total_chars, solve

EXAMPLES_TOTAL = (
    (r'""', 2),
    (r'"abc"', 5),
    (r'"aaa\"aaa"', 10),
    (r'"\x27"', 6),
)
EXAMPLES_MEMORY = (
    ('""', 0),
    ('"abc"', 3),
    ('"aaa\"aaa"', 7),
    ('"\x27"', 1),
)
FILE_DATA = b"""
""
"abc"
"aaa\"aaa"
"\x27"
"""
EXAMPLES_FILE = (
    # 23 - 11 = 12
    (FILE_DATA, 12),
)
EXAMPLES_FILE_EXTRA_RAW = (
    # 42 - 23 = 19
    (FILE_DATA, 19),
)


@pytest.mark.parametrize('data,expected', EXAMPLES_TOTAL)
def test_count_total_chars(data, expected):
    assert count_total_chars(data) == expected


@pytest.mark.skip('TODO: Fix paths')
@pytest.mark.parametrize('data,expected', EXAMPLES_MEMORY)
def test_count_in_memory_chars(data, expected):
    assert count_in_memory_chars(data) == expected


@pytest.mark.skip('TODO: Fix paths')
@pytest.mark.parametrize('data,expected', EXAMPLES_FILE)
def test_solve(data, expected):
    import tempfile
    temp_file = tempfile.TemporaryFile()
    temp_file.write(data)
    temp_file.seek(0)
    assert solve(temp_file) == expected


# @pytest.mark.parametrize('data,expected', EXAMPLES_FILE_EXTRA_RAW)
# def test_solve2(data, expected):
#     assert solve2(data) == expected
