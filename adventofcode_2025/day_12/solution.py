"""title

https://adventofcode.com/2025/day/12

"""
import re


def area_generator(data):
    for area in data.strip().split("\n\n")[-1].split('\n'):
        nums = re.findall(r'\d+', area)
        size = (int(nums[0]), int(nums[1]))
        presents = dict()
        for i, n in enumerate(nums[2:]):
            presents[i] = int(n)
        yield size, presents


def get_presents_sizes(data):
    sizes_dict = dict()
    for present in data.strip().split("\n\n")[0:-1]:
        name = int(present[0])
        size = present.count('#')
        sizes_dict[name] = size
    return sizes_dict


def solve(data):
    sizes_dict = get_presents_sizes(data)
    result = 0
    for area in area_generator(data):
        min_presents_area = 0
        area_size = area[0]
        area_presents = area[1]
        for name, count in area_presents.items():
            min_presents_area += count * sizes_dict[name]
        if min_presents_area < area_size[0] * area_size[1]:
            result += 1
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
