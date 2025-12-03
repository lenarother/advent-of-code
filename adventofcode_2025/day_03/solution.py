"""Day 3: Lobby

https://adventofcode.com/2025/day/3

"""


def find_joltage(battery, n=12):
    result_number = ""
    j = 0
    for i in list(range(n - 1, -1, -1)):
        battery_to_test = battery[j: -i or None]
        max_num = max(battery_to_test)
        j += battery_to_test.index(max_num) + 1
        result_number += max_num
    return int(result_number)


def solve(data, n=2):
    return sum(
        find_joltage(battery, n)
        for battery in data.strip().split("\n")
    )


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 2)
    print(f'Example1: {result}')
    result = solve(input_data, 12)
    print(f'Example2: {result}')
