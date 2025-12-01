"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1

"""


def iter_numbers(input_data):
    lines = input_data.strip().split("\n")
    for i in lines:
        yield i[0], int(i[1:])


def solve(data):
    counter = 0
    result = 50
    for d, n in iter_numbers(data):
        n = n % 100

        if d == "L":
            result -= n
            if result < 0:
                result += 100

        elif d == "R":
            result += n
            if result >= 100:
                result -= 100

        if result == 0:
            counter += 1
    return counter


def solve2(data):
    counter = 0
    result = 50

    for d, n in iter_numbers(data):
        previous_result = result
        counter += abs(n // 100)

        n = n % 100
        if n != 0:

            if d == "L":
                result -= n
                if result < 0:
                    result += 100
                    if previous_result != 0:
                        counter += 1

            elif d == "R":
                result += n
                if result >= 100:
                    result -= 100
                    if result != 0:
                        counter += 1

            if result == 0:
                counter += 1

    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    result2 = solve2(input_data)
    print(f'Example1: {result}')
    print(f'Example2: {result2}')
