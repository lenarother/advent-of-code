"""Day 2: Rock Paper Scissors

https://adventofcode.com/2022/day/2

"""
SHAPE_MAP = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS',
}
SHAPE_SCORE = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}
RESULT_MAP = {
    'X': 0,  # lost
    'Y': 3,  # no winner
    'Z': 6,  # won
}


def get_shape_score(shape):
    return SHAPE_SCORE.get(shape)


def get_game_score(opponent_shape, your_shape):
    if opponent_shape == your_shape:
        return 3
    if (opponent_shape, your_shape) == ('SCISSORS', 'PAPER'):
        return 0
    if (opponent_shape, your_shape) == ('PAPER', 'SCISSORS'):
        return 6
    if (opponent_shape, your_shape) == ('PAPER', 'ROCK'):
        return 0
    if (opponent_shape, your_shape) == ('ROCK', 'PAPER'):
        return 6
    if (opponent_shape, your_shape) == ('ROCK', 'SCISSORS'):
        return 0
    if (opponent_shape, your_shape) == ('SCISSORS', 'ROCK'):
        return 6


def get_my_shape(opponent_shape, score):
    if score == 3:  # no winner
        return opponent_shape
    if score == 0:  # need to lose
        if opponent_shape == 'ROCK':
            return 'SCISSORS'
        if opponent_shape == 'SCISSORS':
            return 'PAPER'
        if opponent_shape == 'PAPER':
            return 'ROCK'
    if score == 6:  # need to win
        if opponent_shape == 'ROCK':
            return 'PAPER'
        if opponent_shape == 'SCISSORS':
            return 'ROCK'
        if opponent_shape == 'PAPER':
            return 'SCISSORS'


def score_round(game_round):
    opponent, you = game_round.split(' ')
    opponent = SHAPE_MAP.get(opponent)
    you = SHAPE_MAP.get(you)
    return get_shape_score(you) + get_game_score(opponent, you)


def score_round2(game_round):
    opponent, round_result = game_round.split(' ')
    opponent = SHAPE_MAP.get(opponent)
    round_result = RESULT_MAP.get(round_result)
    you = get_my_shape(opponent, round_result)
    return get_shape_score(you) + get_game_score(opponent, you)


def solve(data, scoring_function=score_round):
    return sum([scoring_function(i) for i in data.strip().split('\n')])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, score_round2)
    print(f'Example2: {result}')
