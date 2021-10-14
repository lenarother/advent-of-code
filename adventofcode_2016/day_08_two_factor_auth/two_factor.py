"""Day 8: Two-Factor Authentication

https://adventofcode.com/2016/day/8

The magnetic strip on the card you swiped encodes
a series of instructions for the screen; these instructions
are your puzzle input. The screen is 50 pixels wide
and 6 pixels tall, all of which start off,
and is capable of three somewhat peculiar operations:

- rect AxB turns on all of the pixels in a rectangle
  at the top-left of the screen which is A wide and B tall.
- rotate row y=A by B shifts all of the pixels in row A
  (0 is the top row) right by B pixels. Pixels that would
  fall off the right end appear at the left end of the row.
- rotate column x=A by B shifts all of the pixels in column A
  (0 is the left column) down by B pixels. Pixels that would
  fall off the bottom appear at the top of the column.

"""
import re


class Screen:
    cols = None
    rows = None

    def __init__(self, cols=7, rows=3):
        self.cols = cols
        self.rows = rows
        self.screen = self.get_empty_screen()
        self.rules = {
            'rect': r'rect (\d+)x(\d+)',
            'rotate column': r'rotate column x=(\d+) by (\d+)',
            'rotate row': r'rotate row y=(\d+) by (\d+)',
        }
        self.instructions = {
            'rect': self.rect,
            'rotate column': self.rotate_column,
            'rotate row': self.rotate_row,
        }

    def get_empty_screen(self):
        return '.' * (self.cols * self.rows)

    def parse_instruction(self, instruction):
        for k, v in self.rules.items():
            if instruction.startswith(k):
                return k, *map(int, re.findall(v, instruction)[0])

    def rect(self, a, b):
        rectangle = f'{(b * (("#" * a) + ("." * (self.cols - a)))) + (self.rows - b) * ("." * self.cols)}'  # noqa
        self.screen = ''.join([
            '#' if '#' in [i, j] else '.'
            for i, j in zip(rectangle, self.screen)]
        )

    def rotate_column(self, a, b):
        col = self.screen[a::self.cols]
        screen_list = list(self.screen)
        for i, x in enumerate(col):
            pos = (a + (self.cols * (i + b))) % (self.cols * self.rows)
            screen_list[pos] = x
        self.screen = ''.join(screen_list)

    def rotate_row(self, a, b):
        start = a * self.cols
        stop = start + self.cols
        row = self.screen[start:stop]
        assert len(row) == self.cols
        new_row = row[-b:] + row[:-b]
        assert len(new_row) == self.cols
        self.screen = self.screen[:start] + new_row + self.screen[stop:]

    def update_screen(self, instruction):
        itype, a, b = self.parse_instruction(instruction)
        self.instructions[itype](a, b)

    def display(self, instructions):
        for i in instructions:
            self.update_screen(i)

    def count_pixels(self):
        return self.screen.count('#')

    def show_screen(self):
        for x in range(0, len(self.screen), self.cols):
            print(self.screen[x:x+self.cols])


def display(instructions, cols=7, rows=3):
    screen = Screen(cols, rows)
    screen.display(instructions)
    return screen.screen


def count_pixels(instructions, cols=7, rows=3):
    screen = Screen(cols, rows)
    screen.display(instructions)
    return screen.count_pixels()


if __name__ == '__main__':
    f = open('input_data.txt')
    print(f'Example1: {count_pixels(f, 50, 6)}')

    f = open('input_data.txt')
    screen = Screen(50, 6)
    screen.display(f)
    screen.show_screen()
