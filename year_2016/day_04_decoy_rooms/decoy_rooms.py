"""Day 4: Security Through Obscurity

https://adventofcode.com/2016/day/4

Each room consists of an encrypted name
(lowercase letters separated by dashes) followed by a dash,
a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters
in the encrypted name, in order, with ties broken by alphabetization.
For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room
    because the most common letters are a (5), b (3),
    and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because
    although the letters are all tied (1 of each),
    the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.

To decrypt a room name, rotate each letter forward through the alphabet
a number of times equal to the room's sector ID.
A becomes B, B becomes C, Z becomes A, and so on.
Dashes become spaces.

For example, the real name for
qzmt-zixmtkozy-ivhz-343 is very encrypted name.
"""
import re
from collections import Counter

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
SPECIAL_CHARACTERS = '- '


def split_room(room):
    return re.findall(r'([a-z,-]+)-(\d+)\[([a-z]+)\]', room)[0]


def is_checksum_valid(decoy, checksum):
    decoy_dict = Counter(re.sub('-', '', decoy))
    decoy_sorted = sorted(decoy_dict.items(), key=lambda x: (-x[1], x[0]))
    return checksum == ''.join(i[0] for i in decoy_sorted)[:5]


def get_room_id(room):
    decoy, id, checksum = split_room(room)
    return int(id) if is_checksum_valid(decoy, checksum) else 0


def get_room_id_sum(rooms):
    return sum(map(get_room_id, rooms))


def decrypt_character(ch, id):
    cipher_base = SPECIAL_CHARACTERS if ch in SPECIAL_CHARACTERS else ALPHABET
    current_index = cipher_base.index(ch)
    return cipher_base[(current_index + id) % len(cipher_base)]


def get_room_name(encrypted, id):
    decrypted = ''
    for ch in encrypted:
        decrypted += decrypt_character(ch, id)
    return decrypted


if __name__ == '__main__':
    f = open('input_data.txt')
    result = get_room_id_sum(f)
    print(f'Example1: {result}')

    f = open('input_data.txt')
    for room in f:
        decoy, id, checksum = split_room(room)
        if is_checksum_valid(decoy, checksum):
            name = get_room_name(decoy, int(id))
            if name == 'northpole object storage':
                print(f'Example2: {id}')
