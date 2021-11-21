import pytest

from .solution import get_room_id, get_room_id_sum, get_room_name

EXAMPLES = (
    ('aaaaa-bbb-z-y-x-123[abxyz]', 123),
    ('a-b-c-d-e-f-g-h-987[abcde]', 987),
    ('not-a-real-room-404[oarel]', 404),
    ('totally-real-room-200[decoy]', 0),
)

EXAMPLES_SUM = (
    (['aaaaa-bbb-z-y-x-123[abxyz]'], 123),
    (['aaaaa-bbb-z-y-x-123[abxyz]', 'aaaaa-bbb-z-y-x-123[abxyz]'], 246),
    ([
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
     ], 1514),
)

EXAMPLES_NAME = (
    ('a', 1, 'b'),
    ('b', 1, 'c'),
    ('a', 2, 'c'),
    ('a', 28, 'c'),
    ('-', 1, ' '),
    ('-', 2, '-'),
    ('-', 3, ' '),
    ('aa', 1, 'bb'),
    ('qzmt-zixmtkozy-ivhz', 343, 'very encrypted name'),
)


@pytest.mark.parametrize('room,id', EXAMPLES)
def test_get_room_id(room, id):
    assert get_room_id(room) == id


@pytest.mark.parametrize('room_list,expected', EXAMPLES_SUM)
def test_get_room_id_sum(room_list, expected):
    assert get_room_id_sum(room_list) == expected


@pytest.mark.parametrize('encrypted,id,decrypted', EXAMPLES_NAME)
def test_get_room_name(encrypted, id, decrypted):
    assert get_room_name(encrypted, id) == decrypted
