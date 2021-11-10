"""Day 19: An Elephant Named Joseph

https://adventofcode.com/2016/day/19

"""


def solve_left(data):
    data = range(1, data + 1)
    first = 0
    while len(data) > 1:
        last = data[-1]
        data = data[first::2]
        first = 1 if last == data[-1] else 0
    return data[0]


def get_winner(elves, previous_winner):
    eliminate = (elves // 2) + 1
    winner = previous_winner + 1
    winner += int(winner >= eliminate)
    return winner % elves or elves


def solve_across(elves):
    """
 1  | 1
 2  | eliminate 2 --> 1
 3  | eliminate 2 --> 1 from 1 --> 3
 4  | eliminate 3 --> 3 from 2 --> 1
 5  | eliminate 3 --> 1 from 2 --> 2 *
 6  | eliminate 4 --> 2 from 2 --> 3 *
 7  | eliminate 4 --> 3 from 2 --> 5
 8  | eliminate 5 --> 5 from 2 --> 7
 9  | eliminate 5 --> 7 from 2 --> 9
10  | eliminate 6 --> 9 from 2 --> 1
11  | eliminate 6 --> 1 from 2 --> 2 *
12  | eliminate 7 --> 2 from 2 --> 3 *
len | (len // 2) + 1 --> (1 + previous result) % len + int()
    """
    # TOO SLOW
    # from collections import deque
    # data = deque(range(1, data + 1))
    # while len(data) > 1:
    #     remove_index = len(data) // 2
    #     del(data[remove_index])
    #     first = data.popleft()
    #     data.append(first)
    # return data[0]
    winner = 1
    for n in range(2, elves + 1):
        winner = get_winner(n, winner)
    return winner


def solve(data, across=False):
    if across:
        return solve_across(data)
    return solve_left(data)


if __name__ == '__main__':
    result = solve(3014387)
    print(f'Example1: {result}')

    result = solve(3014387, True)
    print(f'Example1: {result}')
