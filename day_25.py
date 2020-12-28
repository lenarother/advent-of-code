"""Day 25

https://adventofcode.com/2020/day/25

"""


def transform(subject_number, loop_size):
    value = 1
    while loop_size:
        value = value * subject_number
        value = value % 20201227
        loop_size = loop_size - 1
    return value  # pub key


def find_loop_size(subject_number, pub_key):
    value = 1
    loop_size = 0
    while 1:
        value = value * subject_number
        value = value % 20201227
        loop_size += 1
        if value == pub_key:
            return loop_size


def find_encription_key(subject_number, pub_key_door, pub_key_card):
    card_loop_size = find_loop_size(subject_number, pub_key_card)
    return transform(pub_key_door, card_loop_size)


if __name__ == '__main__':

    # Part 1
    result = find_encription_key(7, 17807724, 5764801)
    print('Part 1 - Test set 1: ', result)  # 14897079

    result = find_encription_key(7, 10441485, 1004920)
    print('Part 1 - Result: ', result)

    # card
    # result = transform(7, 8)
    # print(result)
    # print('Expected: 5764801')
    #
    # # door
    # result = transform(7, 11)
    # print(result)
    # print('Expected: 17807724')
    #
    # # exnription_key
    # result = transform(5764801, 11)
    # print(result)
    # print('Expected: 14897079')
    # Part 1
    # result = solve1('inputdata/day-22-1.txt')
    # print('Part 1 - Test set 1: ', result)
    #
    # result = solve1('inputdata/day-22-2.txt')
    # print('Part 1 - Result: ', result)
    #
    # # Part 2
    # result = solve2('inputdata/day-22-1.txt')
    # print('Part 2 - Test set 1: ', result)
    #
    # result = solve2('inputdata/day-22-2.txt')
    # print('Part 2 - Result: ', result)
