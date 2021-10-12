"""Day 22: Crab Combat

https://adventofcode.com/2020/day/22

"""

from copy import deepcopy


def parse_input(filename):
    data = open(filename).read().strip().split('\n\n')
    deck1 = list(map(int, data[0].split('\n')[1:]))
    deck2 = list(map(int, data[1].split('\n')[1:]))
    return deck1, deck2


def playcombat(d1, d2):
    if not d1 or not d2:
        return sum([
            (count + 1) * c for count, c in enumerate((d1 or d2)[::-1])
        ])
    p1 = d1.pop(0)
    p2 = d2.pop(0)
    if p1 > p2:
        d1 += [p1, p2]
    else:
        d2 += [p2, p1]
    return playcombat(d1, d2)


class Combat:

    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2

    def play_round(self):
        p1 = self.deck1.pop(0)
        p2 = self.deck2.pop(0)
        if p1 > p2:
            self.deck1 += [p1, p2]
        else:
            self.deck2 += [p2, p1]

    def play(self):
        while len(self.deck1) and len(self.deck2):
            self.play_round()

    def count_score(self):
        deck = self.deck1 or self.deck2
        result = 0
        for counter, card in enumerate(deck[::-1]):
            result += (counter + 1) * card
        return result


def solve1(filename):
    d1, d2 = parse_input(filename)

    game = Combat(d1, d2)
    game.play()
    result = game.count_score()

    # Alternative:
    # result = playcombat(d1, d2)

    return result


class RecursiveCombat(Combat):

    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.past_deck1 = {}
        self.past_deck2 = {}
        self.winer = None
        self.result = None

    def in_memory(self):
        if (tuple(self.deck1) in self.past_deck1) and (
                tuple(self.deck2) in self.past_deck2):
            return True

        self.past_deck1[tuple(self.deck1)] = True
        self.past_deck2[tuple(self.deck2)] = True
        return False

    def play(self):
        while not self.winer:
            self.play_round()
        return self.winer, self.result

    def play_round(self):
        if self.in_memory():
            self.winer = 'p1'
            self.result = self.count_score()
            return
        if len(self.deck1) == 0 or len(self.deck2) == 0:
            self.winer = 'p1' if len(self.deck2) == 0 else 'p2'
            self.result = self.count_score()
            return

        p1 = self.deck1.pop(0)
        p2 = self.deck2.pop(0)

        if p1 <= len(self.deck1) and p2 <= len(self.deck2):
            new_d1 = deepcopy(self.deck1)[:p1]
            new_d2 = deepcopy(self.deck2)[:p2]
            winner, _ = RecursiveCombat(new_d1, new_d2).play()
            if winner == 'p1':
                self.deck1 += [p1, p2]
            else:
                self.deck2 += [p2, p1]

        elif p1 > p2:
            self.deck1 += [p1, p2]

        else:
            self.deck2 += [p2, p1]


def solve2(filename):
    d1, d2 = parse_input(filename)
    game = RecursiveCombat(d1, d2)
    winner, score = game.play()
    return score


if __name__ == '__main__':

    # Part 1
    result = solve1('inputdata/day-22-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = solve1('inputdata/day-22-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = solve2('inputdata/day-22-1.txt')
    print('Part 2 - Test set 1: ', result)

    result = solve2('inputdata/day-22-2.txt')
    print('Part 2 - Result: ', result)
