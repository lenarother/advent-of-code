"""
Maze:

You have a maze given as a string:

##y##
#...#
##x##
#####

You start in the position marked with an x.
Find the way to the exit y.
Return the length of the shortest path.
"""


class MazeException(Exception):
    pass


class Maze:
    MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    WALKABLE = '.y'

    def __init__(self, maze):
        self.maze = maze.lower().strip().split()
        self.start = self.find_position('x')
        self.end = self.find_position('y')
        self.validate_maze()

    def __iter__(self):
        for y, y_el in enumerate(self.maze):
            for x, x_el in enumerate(y_el):
                yield (x, y), x_el

    def validate_maze(self):
        if not self.start:
            raise MazeException('No enterance.')
        if not self.end:
            raise MazeException('No exit.')

    def find_position(self, element):
        for position, el in self:
            if el == element:
                return position

    def find_moves(self, position):
        possible_moves = set()
        x, y = position
        for move in self.MOVES:
            dx, dy = move
            x_check, y_check = x + dx, y + dy
            if self.maze[y_check][x_check] in self.WALKABLE:
                possible_moves.add((x_check, y_check))
        return possible_moves

    def get_neighbour_positions(self, positions):
        candidates = set()
        for position in positions:
            moves = self.find_moves(position)
            candidates = candidates.union(moves)
        return candidates

    def find_path_length(self, max_iter):
        positions = set((self.start,))
        counter = 0

        while self.end not in positions:
            if not max_iter:
                raise MazeException('Max iteration excided.')
            positions = self.get_neighbour_positions(positions)
            counter += 1
            max_iter -= 1

        return counter


def find_path_length(input_maze, max_iter=100):
    maze = Maze(input_maze)
    return maze.find_path_length(max_iter)
