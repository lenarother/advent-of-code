import pytest

from .solution import (
    get_hash_repeated_char,
    hash_generator,
    solve,
    stretch_hash_generator,
)

EXAMPLES = (
    ('abc', 1, 39),
    ('abc', 2, 92),
    ('abc', 64, 22728),
)

EXAMPLES_REPEATS = (
    ('abc', 1, 3, None),
    ('abc', 18, 3, '8'),
    ('abc', 39, 3, 'e'),
    ('abc', 816, 5, 'e'),
    ('abc', 92, 3, '9'),
    ('abc', 200, 3, '9'),
)

EXAMPLES_HASHES = (
    ('abc', 0, '577571be4de9dcce85a041ba0410f29f'),
    ('abc', 1, '23734cd52ad4a4fb877d8a1e26e5df5f'),
    ('abc', 2, '63872b5565b2179bd72ea9c339192543'),

)

EXAMPLES_STRETCH_HASHES = (
    ('abc', 0, 'a107ff634856bb300138cac6568c0f24'),
)


@pytest.mark.parametrize('salt,counter,expected', EXAMPLES)
def test_solve(salt, counter, expected):
    assert solve(salt, counter) == expected


@pytest.mark.parametrize('salt,counter,repeat,expected', EXAMPLES_REPEATS)
def test_get_hash_repeated_char(salt, counter, repeat, expected):
    g = hash_generator(salt)
    for i in range(counter + 1):
        hash_to_check = next(g)
    assert get_hash_repeated_char(hash_to_check, repeat) == expected


@pytest.mark.parametrize('salt,counter,expected', EXAMPLES_HASHES)
def test_hash_generator(salt, counter, expected):
    g = hash_generator(salt)
    for i in range(counter + 1):
        result = next(g)
    assert result == expected


@pytest.mark.parametrize('salt,counter,expected', EXAMPLES_STRETCH_HASHES)
def test_stretch_hash_generator(salt, counter, expected):
    g = stretch_hash_generator(salt)
    for i in range(counter + 1):
        result = next(g)
    assert result == expected
