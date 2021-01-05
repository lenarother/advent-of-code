"""Day 5: Binary Boarding

https://adventofcode.com/2020/day/5

"""


def get_input_list_from_file(filename):
    input = open(filename).readlines()
    return list(map(lambda x: x.strip(), input))


def decode_seat(seat):
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(seat[7:].replace('R', '1').replace('L', '0'), 2)
    return row, column, row * 8 + column


def get_max_seat_id(filename):
    seats = get_input_list_from_file(filename)
    seats.sort(key=lambda seat: decode_seat(seat))
    return decode_seat(seats[-1])[2]


def get_missing_seat(filename):
    seats = get_input_list_from_file(filename)
    seats_ids = sorted([decode_seat(seat)[2] for seat in seats])
    for x, y in zip(seats_ids, seats_ids[1:]):
        if y - x != 1:
            return x + 1


if __name__ =='__main__':
    # Part 1
    assert decode_seat('BFFFBBFRRR') == (70, 7, 567)
    assert decode_seat('FFFBBBFRRR') == (14, 7, 119)
    assert decode_seat('BBFFBBFRLL') == (102, 4, 820)

    result = get_max_seat_id('inputdata/day-05-1.txt')
    print('Part 1 - Result: ', result)

    # # Part 2
    result = get_missing_seat('inputdata/day-05-1.txt')
    print('Part 2 - Result: ', result)
