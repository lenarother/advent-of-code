"""title

https://adventofcode.com/2025/day/5

"""


def get_ingredient_ranges(data):
    for i in data.strip().split('\n\n')[0].split('\n'):
        a, b = i.split('-')
        yield range(int(a), int(b) + 1)


def get_ingredients(data):
    for i in data.strip().split('\n\n')[1].split('\n'):
        yield int(i)


def is_in_range(i, data):
    for r in get_ingredient_ranges(data):
        if i in r:
            return True
    return False


def solve(data):
    result = 0
    for i in get_ingredients(data):
        result += is_in_range(i, data)
    return result


def find_overlaps(myrange, ranges_list):
    overlaps = [myrange]
    rest = []
    for r in ranges_list:
        if myrange.start < r.stop and r.start < myrange.stop:
            overlaps.append(r)
        else:
            rest.append(r)
    return overlaps, rest


def connect_overlaps(overlaps):
    start = []
    end = []
    for r in overlaps:
        start.append(r.start)
        end.append(r.stop)
    return range(min(start), max(end))


def connect_ranges(data):
    ranges = list(get_ingredient_ranges(data))
    counter = len(ranges)
    while counter:
        counter -= 1
        overlaps, rest = find_overlaps(ranges[0], ranges[1:])
        rest.append(connect_overlaps(overlaps))
        ranges = rest
    return ranges


def solve2(data):
    result = 0
    ranges = connect_ranges(data)
    for r in ranges:
        result += len(r)
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example2: {result}')
