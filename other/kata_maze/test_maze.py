import pytest
from maze import Maze, MazeException, find_path_length

MAZE_1 = """
##y##
#...#
##x##
#####
"""

MAZE_2 = """
###
#x#
#.#
#y#
###
"""

MAZE_3 = """
######
#....#
#x...#
#...y#
######
"""

MAZE_4 = """
###
#x#
#y#
###
"""

MAZE_5 = """
###
#x#
#.#
###
"""

MAZE_6 = """
###
#.#
#y#
###
"""

MAZE_7 = """
######
#....#
#Y...#
#...X#
######
"""

MAZE_8 = """
############
#.#.####.###
#.X#..#...##
##....##...#
####.#.###.#
#.##..#.Y#.#
#..##....#.#
##...##.####
############
"""


class TestMaze:

    def test_init_maze(self):
        assert Maze(MAZE_1)

    def test_maze_maze(self):
        maze = Maze(MAZE_1)
        assert isinstance(maze.maze, list)

    @pytest.mark.parametrize(
        'data,expected',
        (
            (MAZE_1, 4),
            (MAZE_2, 5),
        )
    )
    def test_n_rows(self, data, expected):
        maze = Maze(data)
        assert len(maze.maze) == expected

    @pytest.mark.parametrize(
        'data,expected',
        (
            (MAZE_1, 5),
            (MAZE_2, 3),
        )
    )
    def test_n_elements(self, data, expected):
        maze = Maze(data)
        assert len(maze.maze[0]) == expected

    @pytest.mark.parametrize(
        'data,element,expected',
        (
            (MAZE_1, 'x', (2, 2)),
            (MAZE_2, 'x', (1, 1)),
            (MAZE_3, 'x', (1, 2)),
            (MAZE_1, 'y', (2, 0)),
        )
    )
    def test_find_position(self, data, element, expected):
        maze = Maze(data)
        assert maze.find_position(element) == expected

    @pytest.mark.parametrize(
        'data,position,expected',
        (
            (MAZE_1, (2, 2), {(2, 1)}),
            (MAZE_2, (1, 1), {(1, 2)}),
            (MAZE_2, (1, 2), {(1, 3)}),
        )
    )
    def test_find_moves(self, data, position, expected):
        maze = Maze(data)
        assert maze.find_moves(position) == expected

    @pytest.mark.parametrize(
        'maze,expected',
        (
            (MAZE_1, 2),
            (MAZE_2, 2),
            (MAZE_3, 4),
            (MAZE_4, 1),
            (MAZE_7, 4),
            (MAZE_8, 11),
        )
    )
    def test_find_path_length(self, maze, expected):
        assert find_path_length(maze) == expected

    def test_raise_if_maze_has_no_exit(self):
        with pytest.raises(MazeException):
            find_path_length(MAZE_5)

    def test_raise_if_maze_has_no_enterance(self):
        with pytest.raises(MazeException):
            find_path_length(MAZE_6)

    def test_raise_path_length_exided(self):
        with pytest.raises(MazeException):
            find_path_length(MAZE_7, max_iter=3)
