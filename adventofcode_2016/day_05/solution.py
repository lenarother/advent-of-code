"""Day 5: How About a Nice Game of Chess?

https://adventofcode.com/2016/day/5

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input
and an increasing integer index (starting with 0).

A hash indicates the next character in the password
if its hexadecimal representation starts with five zeroes.
If it does, the sixth character in the hash is the next
character of the password.

For example, if the Door ID is abc:

- The first index which produces a hash that starts with five zeroes is
    3231929, which we find by hashing abc3231929; the sixth character
    of the hash, and thus the first character of the password, is 1.
- 5017308 produces the next interesting hash, which starts with 000008f82...,
    so the second character of the password is 8.
- The third time a hash starts with five zeroes is for abc5278568,
    discovering the character f.

"""
import hashlib

PASSWORD_LENGTH = 8


def hash_generator(base):
    counter = 0
    while 1:
        temp = hashlib.md5(f'{base}{counter}'.encode('utf-8')).hexdigest()
        counter += 1
        if temp.startswith('00000'):
            yield temp


def find_code(door_id):
    hash_gen = hash_generator(door_id)
    return ''.join([
        i[5] for i in
        list(next(hash_gen) for _ in range(8))
    ])


def find_sophisticated_code(door_id):
    code = ['_'] * 8
    hash_gen = hash_generator(door_id)
    while code.count('_') > 0:
        temp = next(hash_gen)
        ch5, ch6 = temp[5], temp[6]
        if ch5.isdigit() and int(ch5) < 8 and code[int(ch5)] == '_':
            code[int(ch5)] = ch6
    return ''.join(code)


if __name__ == '__main__':
    result = find_code('cxdnnyjw')
    print(f'Example1: {result}')

    result = find_sophisticated_code('cxdnnyjw')
    print(f'Example1: {result}')
