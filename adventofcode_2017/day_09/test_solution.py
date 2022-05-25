import pytest

from .solution import calculate_score, remove_garbage, solve


@pytest.mark.parametrize(
    'data, expected',
    (
        ('<>', ''),
        ('<random characters>', ''),
        ('<<<<>', ''),
        ('<{!>}>', ''),
        ('<!!>', ''),
        ('<!!!>>', ''),
        ('<{o"i!a,<{i<a>', ''),
        ('<{o"i!a,<{i<a><{o"i!a,<{i<a>', ''),
        ('aaa', 'aaa'),
        ('{{<a>},{<a>},{<a>},{<a>}}', '{{},{},{},{}}'),
        ('{{<!>},{<!>},{<!>},{<a>}}', '{{}}'),
        ('{{<!">}}', '{{}}'),
    )
)
def test_remove_garbage(data, expected):
    result, _ = remove_garbage(data)
    assert result == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('', 0),
        ('aaa', 0),
        ('{{},{},{},{}}', 9),
        ('{{{},{},{{}}}}', 16),
        ('{{}}', 3),
    )
)
def test_calculate_score(data, expected):
    assert calculate_score(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('<>', 0),
        ('<random characters>', 0),
        ('<<<<>', 0),
        ('<{!>}>', 0),
        ('<!!>', 0),
        ('<!!!>>', 0),
        ('<{o"i!a,<{i<a>', 0),
        ('<{o"i!a,<{i<a><{o"i!a,<{i<a>', 0),
        ('aaa', 0),
        ('{{<a>},{<a>},{<a>},{<a>}}', 9),
        ('{{<!>},{<!>},{<!>},{<a>}}', 3),
        ('{{<!">}}', 3),
    )
)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize(
    'data, expected',
    (
        ('<>', 0),
        ('<random characters>', 17),
        ('<<<<>', 3),
        ('<{!>}>', 2),
        ('<!!>', 0),
        ('<!!!>>', 0),
        ('<{o"i!a,<{i<a>', 10),
        ('<{o"i!a,<{i<a><{o"i!a,<{i<a>', 20),
        ('aaa', 0),
    )
)
def test_calculate_garbage_length(data, expected):
    _, result = remove_garbage(data)
    assert result == expected
