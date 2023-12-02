"""title

https://adventofcode.com/2023/day/2

"""
import re

RED = r'(\d+) red'
BLUE = r'(\d+) blue'
GREEN = r'(\d+) green'


class DrawSet:

    def __init__(self, r, b, g):
        self.r = r
        self.b = b
        self.g = g

    def is_possible(self, r, b, g):
        if self.r <= r and self.b <= b and self.g <= g:
            return True
        return False


class Game:

    def __init__(self, id):
        self.id = id
        self.draws = []

    def is_possible(self, r, b, g):
        return all(draw.is_possible(r, b, g) for draw in self.draws)

    def get_power(self):
        return (
            max([draw.r for draw in self.draws]) *
            max([draw.b for draw in self.draws]) *
            max([draw.g for draw in self.draws])
        )


def parse_game(game_str):
    id_str, draw_str = game_str.split(': ')
    id = int(id_str.replace('Game ', ''))
    game = Game(id)
    for draw in draw_str.split(';'):
        red = re.findall(RED, draw)
        blue = re.findall(BLUE, draw)
        green = re.findall(GREEN, draw)
        game.draws.append(
            DrawSet(
                r=int(red[0]) if red else 0,
                b=int(blue[0]) if blue else 0,
                g=int(green[0]) if green else 0,
            )
        )
    return game


def id_of_possible_game(game_str, r, b, g):
    game = parse_game(game_str)
    if game.is_possible(r, b, g):
        return game.id
    return 0


def solve(data):
    return sum([
        id_of_possible_game(game_str, r=12, b=14, g=13)
        for game_str in data.split('\n')
    ])


def solve_2(data):
    return sum([
        parse_game(game_str).get_power()
        for game_str in data.split("\n")
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result_2 = solve_2(input_data)
    print(f'Example2: {result_2}')