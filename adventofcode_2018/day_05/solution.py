"""Day 5: Alchemical Reduction

https://adventofcode.com/2018/day/5

"""
import re


class Unit:

    def __init__(self, letter):
        self.letter = letter
        self.unit_type = letter.lower()
        self.unit_polarity = letter.isupper()
        self.right_neighbour = None
        self.left_neighbour = None

    def __eq__(self, other):
        return self.letter == other.letter

    def __repr__(self):
        left = self.left_neighbour.letter if self.left_neighbour else ''
        right = self.right_neighbour.letter if self.right_neighbour else ''
        return f'{left}-[{self.letter}]-{right}'

    def can_remove(self):
        return (
            self.unit_type == self.right_neighbour.unit_type and
            self.unit_polarity != self.right_neighbour.unit_polarity
        )

    def remove(self):
        if not self.right_neighbour or not self.can_remove():
            raise ValueError('Cannot remove units.')

        if self.left_neighbour:
            after = self.right_neighbour.right_neighbour
            self.left_neighbour.right_neighbour = after
            if after:
                after.left_neighbour = self.left_neighbour
            return self.left_neighbour

        if self.right_neighbour.right_neighbour:
            next_unit = self.right_neighbour.right_neighbour
            next_unit.left_neighbour = None
            return next_unit

        return None


def parse_polymer(data):
    first_unit = Unit(data[0])
    current_unit = first_unit
    for letter in data[1:]:
        new_unit = Unit(letter)
        new_unit.left_neighbour = current_unit
        current_unit.right_neighbour = new_unit
        current_unit = new_unit
    return first_unit


def get_polymer_length(unit=None):
    if not unit:
        return 0

    length = 1
    mode = 'right_neighbour' if unit.right_neighbour else 'left_neighbour'

    while getattr(unit, mode) is not None:
        length += 1
        unit = getattr(unit, mode)
    return length


def get_polymer_sequence(unit=None):
    seq = ''
    if not unit:
        return seq

    mode = 'right_neighbour' if unit.right_neighbour else 'left_neighbour'
    seq += unit.letter

    while getattr(unit, mode) is not None:
        unit = getattr(unit, mode)
        seq += unit.letter
    return seq


def react_polymer(first_unit):
    current_unit = first_unit
    while current_unit.right_neighbour:
        while current_unit and current_unit.can_remove():
            current_unit = current_unit.remove()
            if not current_unit:
                return
            if not current_unit.right_neighbour:
                return current_unit
        current_unit = current_unit.right_neighbour
    return current_unit


def solve(data):
    unit = parse_polymer(data.strip())
    unit = react_polymer(unit)
    return get_polymer_length(unit)


def modified_molecules_generator(molecule):
    for i in set(molecule.lower()):
        yield re.sub(i, '', molecule, flags=re.I)


def solve2(data):
    return min([solve(m) for m in modified_molecules_generator(data.strip())])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result2 = solve2(input_data)
    print(f'Example2: {result2}')
