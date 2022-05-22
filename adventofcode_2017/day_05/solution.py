"""Day 5: A Maze of Twisty Trampolines, All Alike

https://adventofcode.com/2017/day/5

"""


def get_new_offset_increase_1(*args):
    return 1


def get_new_offset_increase_2(offset):
    if offset >= 3:
        return -1
    return 1


def solve(data, get_new_offset=get_new_offset_increase_1):
    nums = list(map(int, data.strip().split('\n')))
    i = 0
    n = 0

    while 1:
        if 0 > i or i >= len(nums):
            return n

        old_i = i
        i += nums[i]
        nums[old_i] += get_new_offset(nums[old_i])
        n += 1


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, get_new_offset_increase_2)
    print(f'Example2: {result}')
