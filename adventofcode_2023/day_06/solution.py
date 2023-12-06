"""Day 6: Wait For It

https://adventofcode.com/2023/day/6

"""


def distance_generator(t):
    for hold in range(0, t + 1):
        yield (t - hold) * hold


def get_n_winning_times(t, distance):
    return len(list(filter(lambda x: x > distance, distance_generator(t))))


def solve():
    return (
        get_n_winning_times(54, 239) *
        get_n_winning_times(70, 1142) *
        get_n_winning_times(82, 1295) *
        get_n_winning_times(75, 1253)
    )


def solve_2():
    return get_n_winning_times(54708275, 239114212951253)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve()
    print(f'Example1: {result}')

    result = solve_2()
    print(f'Example1: {result}')
