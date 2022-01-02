"""Day 21: Dirac Dice

https://adventofcode.com/2021/day/21

"""
import re
from collections import defaultdict
from itertools import cycle

PLAYER = r'Player (\d+) starting position: (\d+)'


class Player:

    def __init__(self, data=None):
        self.id = None
        self.position = 0
        self.score = 0
        if data:
            self.parse(data)

    def __repr__(self):
        return f'<Player {self.id}: {self.score}>'

    def parse(self, data):
        id, start_position = re.findall(PLAYER, data)[0]
        self.id = int(id)
        self.position = int(start_position)


def dice(x=0, counter=1):
    counter = counter
    for i in cycle(range(1, 101)):
        yield (i + x) % 100 or 100, counter
        counter += 1


def make_move(p, d):
    s1, c1 = next(d)
    s2, c2 = next(d)
    s3, c3 = next(d)
    round_score = (sum([s1, s2, s3]) + p.position) % 10 or 10
    p.position = round_score
    p.score += round_score
    return c3


def game(data):
    p1, p2 = data.strip().split('\n')
    p1 = Player(p1)
    p2 = Player(p2)
    d = dice()

    move_counter = 1
    while p1.score < 1000 and p2.score < 1000:
        if move_counter % 2 == 1:
            counter = make_move(p1, d)
        else:
            counter = make_move(p2, d)
        move_counter += 1

    return counter * min([p1.score, p2.score])


def solve(data):
    return game(data)


# PART 2 #

SCORES = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
# GAME: (0: a_position, 1: b_position, 2: a_score, 3: b_score)


def make_move_part2(game, game_count, player, new_games):
    for s in SCORES:
        if player == 'A':
            new_position = (game[0] + s) % 10 or 10
            new_score = game[2] + new_position
            g = (new_position, game[1], new_score, game[3])
        elif player == 'B':
            new_position = (game[1] + s) % 10 or 10
            new_score = game[3] + new_position
            g = (game[0], new_position, game[2], new_score)
        g_count = SCORES[s] * game_count
        new_games[g] += g_count


def play(g):
    winner_a = 0
    winner_b = 0
    games = {g: 1}
    player = 'A'

    while len(games) > 0:
        new_games = defaultdict(int)
        for g in games:
            if g[2] >= 21:
                winner_a += games[g]
            elif g[3] >= 21:
                winner_b += games[g]
            else:
                make_move_part2(g, games[g], player, new_games)
        games = new_games
        player = 'A' if player == 'B' else 'B'

    return max([winner_a, winner_b])


def solve2(data):
    data = re.findall(PLAYER, data)
    g = (int(data[0][1]), int(data[1][1]), 0, 0)
    return play(g)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
