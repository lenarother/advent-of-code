"""Day 23: Amphipod

https://adventofcode.com/2021/day/23

"""
import itertools
from heapq import heappop, heappush

COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

DISTANCE = {
    'A': [2, 1, 1, 3, 5, 7, 8],
    'B': [4, 3, 1, 1, 3, 5, 6],
    'C': [6, 5, 3, 1, 1, 3, 4],
    'D': [8, 7, 5, 3, 1, 1, 2],
}


class Room:

    def __init__(self, id, size, items=None):
        self.id = id
        self.size = size
        self.items = list(items or [])

    def __repr__(self):
        return f'<Room {self.id}{self.size}: {", ".join(list(self.items))}>'

    def __len__(self):
        return len(self.items)

    @property
    def is_ready(self):
        return len(set(self.items)) == 1 and self.items[0] == self.id

    def pop(self):
        if self.is_ready:
            raise IndexError('Room is already OK.')
        item = self.items.pop(0)
        cost = COST[item] * (self.size - len(self.items))
        return item, cost

    def can_add(self, item):
        if len(self) == self.size:
            return False
        if item != self.id:
            return False
        if len(self) > 0 and not self.is_ready:
            return False
        return True

    def add(self, item):
        if not self.can_add(item):
            raise ValueError(f'Cannot add item {item} to room {self}')
        cost = COST[item] * (self.size - len(self.items))
        self.items.append(item)
        return cost


class Hallway:

    def __init__(self, slots=7):
        self.slots = {k: None for k in range(slots)}
        assert len(self.slots) == slots

    def __repr__(self):
        return f'<Hallway: {len(self.slots)}>'

    def possible_positions(self, door):
        first = DISTANCE[door].index(1)
        for p in range(first + 1, 7):
            if self.slots[p] is not None:
                break
            yield p
        for p in range(first, -1, -1):
            if self.slots[p] is not None:
                break
            yield p

    def add(self, fish, position, door):
        if position not in self.possible_positions(door):
            raise ValueError('Cannot add fish on this position.')
        self.slots[position] = fish
        return COST[fish] * DISTANCE[door][position]

    def remove(self, position):
        fish = self.slots[position]
        self.slots[position] = None
        cost = DISTANCE[fish][position] * COST[fish]
        return cost

    def is_path_free(self, door, position):
        door_position = DISTANCE[door].index(1)
        if position > door_position:
            door_position += 1

        for p in range(
                min(position, door_position),
                max(position, door_position) + 1
        ):
            if p == position:
                continue
            if self.slots[p] is not None:
                return False

        return True

    def possible_removals(self):
        for k, v in self.slots.items():
            if v and self.is_path_free(v, k):
                yield k, v


class FishSort:

    def __init__(self):
        self.rooms = {}
        self.hallway = None
        self.cost = 0

    def __repr__(self):
        h = ''.join([
            '.' if x is None else x
            for x in self.hallway.slots.values()
        ])
        rooms = ' '.join([
            (
                f'R_{self.rooms[r].id}-'
                f'{"".join([i for i in self.rooms[r].items])}'
            )
            for r in sorted(self.rooms)
        ])
        return f'<FishSort: H-{h} {rooms}>'

    def __hash__(self):
        return hash(f'{self}')

    def done(self):
        for room in self.rooms.values():
            if not room.is_ready or len(room) < room.size:
                return False
        return True

    def possible_moves(self):
        for position, fish in self.hallway.possible_removals():
            if self.rooms[fish].can_add(fish):
                fs = FishCopy.fish_sort(self)
                fs.cost += fs.hallway.remove(position)
                fs.cost += fs.rooms[fish].add(fish)
                yield fs
        for room in self.rooms.values():
            if not room.is_ready and len(room.items) > 0:
                for p in self.hallway.possible_positions(room.id):
                    fs = FishCopy.fish_sort(self)
                    fs_room = fs.rooms[room.id]
                    fish, cost = fs_room.pop()
                    fs.cost += cost
                    fs.cost += fs.hallway.add(
                        fish=fish,
                        position=p,
                        door=room.id
                    )
                    yield fs


class FishCopy:

    @staticmethod
    def room(room):
        return Room(
            id=room.id,
            size=room.size,
            items=[x for x in room.items]
        )

    @staticmethod
    def hallway(hallway):
        h = Hallway()
        h.slots = {k: v for k, v in hallway.slots.items()}
        return h

    @staticmethod
    def fish_sort(fish_sort):
        new_fish_sort = FishSort()
        new_fish_sort.cost = fish_sort.cost
        new_fish_sort.rooms = {
            k: FishCopy.room(v)
            for k, v in fish_sort.rooms.items()
        }
        new_fish_sort.hallway = FishCopy.hallway(fish_sort.hallway)
        return new_fish_sort


class HeapFish:
    """From: https://docs.python.org/3/library/heapq.html"""

    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        """Mark an existing task as self.REMOVED.
        Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """Remove and return the lowest priority task.
        Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


def solve(fish_sort):
    visited = set()
    candidates = HeapFish()
    candidates.add_task(fish_sort, 0)

    while candidates:
        fish_sort = candidates.pop_task()
        if str(fish_sort) not in visited:
            visited.add(str(fish_sort))
            if fish_sort.done():

                return fish_sort.cost

            else:
                for i in fish_sort.possible_moves():
                    if str(i) not in visited:
                        candidates.add_task(i, i.cost)


if __name__ == '__main__':
    # # --- Part 1 --- #
    fs = FishSort()
    fs.hallway = Hallway()
    fs.rooms = {
        'A': Room('A', 2, 'DC'),
        'B': Room('B', 2, 'CD'),
        'C': Room('C', 2, 'AA'),
        'D': Room('D', 2, 'BB'),
    }
    result = solve(fs)
    print(f'Example1: {result}')

    # --- Part 2 --- #
    fs = FishSort()
    fs.hallway = Hallway()
    fs.rooms = {
        'A': Room('A', 4, 'DDDC'),
        'B': Room('B', 4, 'CCBD'),
        'C': Room('C', 4, 'ABAA'),
        'D': Room('D', 4, 'BACB'),
    }
    result = solve(fs)
    print(f'Example2: {result}')
