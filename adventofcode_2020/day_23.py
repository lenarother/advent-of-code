"""Day 23: Crab Cups

https://adventofcode.com/2020/day/23

"""


class Game:

    def get_destination_cup(self, current_cup, cups):
        destination = current_cup - 1
        if destination in cups:
            return destination
        if destination >= min(cups):
            return self.get_destination_cup(destination, cups)
        return max(cups)

    def play_round(self, cups):
        current_cup = cups[0]
        selected_cups = cups[1:4]
        cups = [cups[0]] + cups[4:]
        destination_cup = self.get_destination_cup(current_cup, cups)
        destination_cup_index = cups.index(destination_cup)
        cups = (
            cups[:destination_cup_index + 1] +
            selected_cups +
            cups[destination_cup_index + 1:]
        )
        old_current = cups.pop(0)
        cups.append(old_current)
        return cups

    def play(self, label, rounds):
        cups = [int(x) for x in label]

        while rounds:
            cups = self.play_round(cups)
            rounds = rounds - 1

        start_index = cups.index(1)
        result = cups[start_index + 1:] + cups[:start_index]
        return ''.join(map(str, result))


class Cup:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        lstr = self.left.label if self.left else 'None'
        rstr = self.right.label if self.right else 'None'
        return f'{lstr}-{self.label}-{rstr}'


class GameWithPointers:

    def __init__(self, cups_list):
        self.cups_list = cups_list
        self.cups = self.init_cups(cups_list)

        # Game state:
        self.current = None
        self.selected = None
        self.destination = None

    def init_cups(self, cups_list):
        result = {}
        for counter, cup in enumerate(cups_list):
            current = Cup(label=cup)
            result[cup] = current
            if counter > 0:
                previous = result[cups_list[counter - 1]]
                current.left = previous
                previous.right = current
            if counter == len(cups_list) - 1:
                first = result[cups_list[0]]
                first.left = current
                current.right = first
        return result

    def set_current(self):
        if self.current:
            self.current = self.current.right
        else:
            self.current = self.cups[self.cups_list[0]]

    def select_cups(self):
        first = self.current.right
        second = first.right
        third = second.right
        fourth = third.right

        self.selected = [first, second, third]

        self.current.right = fourth
        fourth.left = self.current

    def set_destination(self, destination=None):
        if destination is None:
            destination = self.current.label - 1
        if destination in [cup.label for cup in self.selected]:
            return self.set_destination(destination - 1)
        elif destination not in self.cups.keys():
            return self.set_destination(max(self.cups.keys()))
        else:
            self.destination = self.cups[destination]

    def insert_selected(self):
        after_destination = self.destination.right
        self.destination.right = self.selected[0]
        self.selected[0].left = self.destination
        after_destination.left = self.selected[2]
        self.selected[2].right = after_destination

    def play_round(self):
        self.set_current()
        self.select_cups()
        self.set_destination()
        self.insert_selected()

    def play(self, rounds):
        while rounds:
            self.play_round()
            rounds = rounds - 1

        cup_1 = self.cups[1]
        first = cup_1.right
        second = first.right

        return first.label * second.label


def solve(labels):
    # Part 2
    labels = [int(x) for x in labels]
    labels_max = max(labels)
    inp = labels + list(range(labels_max + 1, 1000001))
    game = GameWithPointers(inp)
    result = game.play(10000000)
    return result


if __name__ == '__main__':

    # Part 1
    assert Game().play('389125467', 10) == '92658374'
    assert Game().play('389125467', 100) == '67384529'

    result = Game().play('487912365', 100)
    print('Part 1 - Result: ', result)

    # Part 2
    assert solve('389125467') == 149245887792

    result = solve('487912365')
    print('Part 2 - Result: ', result)
