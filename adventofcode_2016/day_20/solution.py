"""Day 20: Firewall Rules

https://adventofcode.com/2016/day/20

"""
import re
from collections import deque


def merge(data):
    if not data:
        return data

    results = []
    data = deque(sorted(data))
    low, high = data.popleft()

    while data:
        n_low, n_high = data.popleft()
        if low <= n_low <= (high + 1):
            high = max(high, n_high)
        else:
            results.append((low, high))
            low, high = n_low, n_high
    results.append((low, high))

    return results


def get_merged_limits(data):
    nums = re.findall(r'(\d+)', data)
    limits = [
        (int(low), int(high))
        for low, high in zip(nums[:-1:2], nums[1::2])
    ]
    return deque(merge(limits))


def get_lowest_ip(data):
    merged_limits = get_merged_limits(data)
    x, y = merged_limits.popleft()

    if x > 0:
        return 0
    return y + 1


def count_possible_ids(data, max_ip):
    merged_limits = get_merged_limits(data)
    low, high = merged_limits.popleft()
    ip_counter = low

    while merged_limits:
        n_low, n_high = merged_limits.popleft()
        ip_counter += n_low - high - 1
        high = n_high

    ip_counter += max_ip - high
    return ip_counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = get_lowest_ip(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = count_possible_ids(input_data, 4294967295)
    print(f'Example2: {result}')
