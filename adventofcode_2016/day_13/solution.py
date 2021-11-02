"""Day 13: A Maze of Twisty Little Cubicles

https://adventofcode.com/2016/day/13

"""


class Maze:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, base):
        self.base = base

    def validate_position(self, x, y):
        if x < 0 or y < 0:
            return False

        eq_sum = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + self.base
        ones = bin(eq_sum).count('1')
        return ones % 2 == 0

    def find_moves(self, position):
        possible_moves = set()
        x, y = position
        for move in self.MOVES:
            dx, dy = move
            x_check, y_check = x + dx, y + dy
            if self.validate_position(x_check, y_check):
                possible_moves.add((x_check, y_check))
        return possible_moves

    def get_neighbour_positions(self, positions):
        candidates = set()
        for position in positions:
            moves = self.find_moves(position)
            candidates = candidates.union(moves)
        return candidates

    def find_path_length(self, start, exit=None, max_iterations=None):
        exit = exit or (-1, -1)  # can never be found
        positions = set((start,))
        all_positions = set((start,))
        counter = 0

        while exit not in positions:
            if max_iterations is not None and counter == max_iterations:
                return len(all_positions)
            positions = self.get_neighbour_positions(positions)
            all_positions = all_positions.union(positions)
            counter += 1

        return counter

    def count_locations(self, start, moves_count):
        return self.find_path_length(start, max_iterations=moves_count)


if __name__ == '__main__':
    m = Maze(1362)
    result = m.find_path_length((1, 1), (31, 39))
    print(f'Example1: {result}')

    m = Maze(1362)
    result = m.find_path_length((1, 1), max_iterations=50)
    print(f'Example2: {result}')
