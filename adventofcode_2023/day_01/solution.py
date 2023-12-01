"""Day 1: Trebuchet?!

https://adventofcode.com/2023/day/1

"""
WORDS_MAP_PART_1 = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

WORDS_MAP_PART_2 = {
    ** WORDS_MAP_PART_1,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_num_from_line(line, words_map=WORDS_MAP_PART_2):
    nums_spelled = list(filter(lambda x: x in line, words_map.keys()))
    nums_spelled_left = sorted(nums_spelled, key=lambda x: line.index(x))
    nums_spelled_right = sorted(nums_spelled, key=lambda x: line.rindex(x))
    if len(nums_spelled) == 0:
        return 0
    return int(f"{words_map[nums_spelled_left[0]]}{words_map[nums_spelled_right[-1]]}")


def solve(data, words_map=WORDS_MAP_PART_2):
    return sum([get_num_from_line(l, words_map) for l in data.split('\n')])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    # Part 1
    result = solve(input_data, words_map=WORDS_MAP_PART_1)
    print(f'Example1: {result}')

    # Part 2
    result = solve(input_data)
    print(f'Example1: {result}')
