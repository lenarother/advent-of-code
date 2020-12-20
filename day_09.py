"""Day 9

https://adventofcode.com/2020/day/9

"""

def parse_input(filename):
    return list(map(int, open(filename).read().strip().split('\n')))


def check_num(num, preamble):
    # Part 1
    for x in preamble:
        y = num - x
        if y < 0:
            continue
        if y in preamble:
            if x != y:
                return True
            elif x == y and preamble.count(x) > 1:
                return True
    return False


def find_invalid_num(data, preamble_size, position=0):
    # Part 1
    num = data[position + preamble_size]
    preamble = data[position:position + preamble_size]
    result = check_num(num, preamble)
    if result is False:
        return num
    position += 1
    return find_invalid_num(data, preamble_size, position)


def find_subset_for_invalid_num(data, num):
    # Part 2
    subset = []
    for x in data:
        subset.append(x)

        subset_sum = sum(subset)
        if subset_sum == num:
            return subset
        while subset_sum > num:
            subset = subset[1:]
            subset_sum = sum(subset)

        if subset_sum == num:
            return subset


def break_xmas_code(data, preamble_size):
    # Part 2
    invalid_num = find_invalid_num(data, preamble_size)
    subset = find_subset_for_invalid_num(data, invalid_num)
    return min(subset) + max(subset)


if __name__ =='__main__':

    # Input
    input1 = parse_input('inputdata/day-09-1.txt')
    input2 = parse_input('inputdata/day-09-2.txt')

    # Part 1
    result = find_invalid_num(input1, 5)
    print('Part 1 - Test set 1: ', result)

    result = find_invalid_num(input2, 25)
    print('Part 1 - Result: ', result)

    # # Part 2
    result = break_xmas_code(input1, 5)
    print('Part 2 - Test set 1: ', result)

    result = break_xmas_code(input2, 25)
    print('Part 2 - Result: ', result)
