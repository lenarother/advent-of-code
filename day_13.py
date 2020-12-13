"""Day 13

https://adventofcode.com/2020/day/13

"""

from functools import reduce
import math
import sys

timestamp = 939
ids = ['7', '13', 'x', 'x', '59', 'x', '31', '19']

timestamp2 = 1005162
ids2 = [
    '19', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '41', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', 'x', '823', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '23', 'x', 'x',
    'x', 'x', 'x', 'x', 'x', 'x', '17', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', '29', 'x', '443', 'x', 'x', 'x', 'x', 'x', '37', 'x', 'x',
    'x', 'x', 'x', 'x', '13'
]


def calculate_bus_time(bus, timestamp):
    # Part 1
    if timestamp % bus == 0:
        return 0
    return bus - (timestamp % bus)


def find_bus(timestamp, bus_list):
    # Par 1
    results = []
    results_id = []
    for bus in bus_list:
        if bus.isdigit():
            result = calculate_bus_time(int(bus), timestamp)
            results.append(result)
            results_id.append(int(bus))
    min_wait_time = min(results)
    min_wait_time_index = results.index(min_wait_time)
    return min_wait_time * results_id[min_wait_time_index]


def check(a, b, mod, step):
    # Part 2
    if a % b == mod:
        return a
    return check(a + step, b, mod, step)


def get_delay(b, t):
    # Part 2
    if b == t:
        r = 0
    elif b > t:
        r = b - t
    else:
        r = b - (t % b)
    return r


def find_time(ids):
    # Part 2
    result_ids = []
    delays = []

    for counter, bus in enumerate(ids):
        if bus.isdigit():
            result_ids.append(int(bus))
            delays.append(get_delay(int(bus), counter))

    step = result_ids[0]
    t = result_ids[0]

    for x in range(len(result_ids) - 1):
        t = check(t, result_ids[x+1], delays[x+1], step)
        step = step * result_ids[x+1]
    return t


if __name__ =='__main__':

    # Part 1
    result = find_bus(timestamp, ids)
    print('Part 1 - Test set 1: ', result)

    result = find_bus(timestamp2, ids2)
    print('Part 1 - Result: ', result)

    # Part 2
    # Test
    assert find_time(['17', 'x', '13', '19']) == 3417
    assert find_time(['67', '7', '59', '61']) == 754018
    assert find_time(['67', '7', 'x', '59', '61']) == 1261476
    assert find_time(['1789', '37', '47', '1889']) == 1202161486

    result = find_time(ids)
    print('Part 2 - Test set 1: ', result)

    result = find_time(ids2)
    print('Part 2 - Result: ', result)
