import pytest

from .solution import FishSort, Hallway, Room, solve


def test_solve_1():
    fs = FishSort()
    fs.hallway = Hallway()
    fs.rooms = {
        'A': Room('A', 1, 'B'),
        'B': Room('B', 1, 'A'),
    }
    assert solve(fs) == 46


def test_solve_2():
    fs = FishSort()
    fs.hallway = Hallway()
    fs.rooms = {
        'A': Room('A', 2, 'BB'),
        'B': Room('B', 2, 'AA'),
        'C': Room('C', 2, 'CC'),
        'D': Room('D', 2, 'DD'),
    }
    assert solve(fs) == 114


def test_solve_3():
    fs = FishSort()
    fs.hallway = Hallway()
    fs.rooms = {
        'A': Room('A', 2, 'BA'),
        'B': Room('B', 2, 'CD'),
        'C': Room('C', 2, 'BC'),
        'D': Room('D', 2, 'DA'),
    }
    assert solve(fs) == 12521


class TestRoom:

    def test_room(self):
        assert f'{Room("A", 2, "AB")}' == '<Room A2: A, B>'

    def test_pop(self):
        room = Room('A', 2, 'AB')
        assert room.pop() == ('A', 1)
        assert room.pop() == ('B', 20)
        with pytest.raises(IndexError):
            room.pop()

    def test_pop_ready(self):
        room = Room('A', 2, 'A')
        with pytest.raises(IndexError):
            room.pop()
        room = Room('A', 4, 'AAAA')
        with pytest.raises(IndexError):
            room.pop()

    def test_add(self):
        room = Room('A', 2)
        cost = room.add('A')
        assert cost == 2
        assert room.items == ['A']
        cost = room.add('A')
        assert cost == 1
        assert room.items == ['A', 'A']
        with pytest.raises(ValueError):
            room.add('A')

    def test_add_wrong_item_raises(self):
        room = Room('A', 2)
        with pytest.raises(ValueError):
            room.add('B')

    def test_add_to_not_ready_raises(self):
        room = Room('A', 2, 'B')
        with pytest.raises(ValueError):
            room.add('A')


class TestHallway:

    def test_hallway(self):
        assert f'{Hallway()}' == '<Hallway: 7>'

    def test_add(self):
        h = Hallway()
        assert h.add(fish='A', position=3, door='D') == 3

    def test_possible_positions(self):
        h = Hallway()
        assert set(h.possible_positions(door='D')) == {0, 1, 2, 3, 4, 5, 6}

        h.add(fish='A', position=3, door='D')
        assert set(h.possible_positions('D')) == {4, 5, 6}

        with pytest.raises(ValueError):
            h.add(fish='A', position=2, door='D')

    def test_remove(self):
        h = Hallway()
        h.add(fish='A', position=3, door='D')
        assert h.remove(3) == 3

        with pytest.raises(KeyError):
            assert h.remove(3) == 3

    def test_possible_removals(self):
        h = Hallway()
        assert set(h.possible_removals()) == set()

        h.add(fish='A', position=3, door='D')
        assert set(h.possible_removals()) == {(3, 'A')}

        h.add(fish='C', position=2, door='A')
        assert set(h.possible_removals()) == set()


class TestFishSort:

    def test_fish_sort(self):
        room_a = Room('A', 1, 'B')
        room_b = Room('B', 1, 'A')
        fs = FishSort()
        fs.hallway = Hallway()
        fs.rooms = {
            'A': room_a,
            'B': room_b,
        }
        assert f'{fs}' == '<FishSort: H-....... R_A-B R_B-A>'
