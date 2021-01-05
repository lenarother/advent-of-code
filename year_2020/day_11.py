import pprint
from operator import itemgetter


DIRECTIONS = {
    'left': {'x': -1, 'y': 0},
    'right': {'x': 1, 'y': 0},
    'top': {'x': 0, 'y': 1},
    'down': {'x': 0, 'y': -1},
    'topleft': {'x': -1, 'y': 1},
    'topright': {'x': 1, 'y': 1},
    'downleft': {'x': -1, 'y': -1},
    'downright': {'x': 1, 'y': -1},
}


class Config:

    def __init__(self, standup_treshold=4, look_beyond_dots=False):
        self.standup_treshold = standup_treshold
        self.look_beyond_dots = look_beyond_dots


class Seat:

    def __init__(self, x, y, state, changed=False):
        self.x = x
        self.y = y
        self.state = state
        self.changed = changed
        self.position = (x, y)

    def __repr__(self):
        return self.state

    def __bool__(self):
        return self.state == '#'

    def get_adjacent_positions(self):
        seats = [
            (self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1),
            (self.x - 1, self.y), (self.x + 1, self.y),
            (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1),
        ]
        result = []
        for x, y in seats:
            if x > 0 and y > 0:
                result.append((x, y))
        return result


class Rules:

    def rule1(self, seat, adjacent_seats):
        """Empty -> occupied

        If a seat is empty (L) and there are no occupied seats adjacent to it,
        the seat becomes occupied.

        """
        if seat.state != 'L' or any(map(bool, adjacent_seats)):
            return None
        return '#'

    def rule2(self, seat, adjacent_seats, standup_treshold):
        """Occupied -> Empty

        If a seat is occupied (#) and four or more seats adjacent to it are
        also occupied, the seat becomes empty.

        """
        if seat.state != '#' or sum(map(bool, adjacent_seats)) < standup_treshold:
            return None
        return 'L'

    def apply(self, seat, adjacent_seats, standup_treshold=4):
        state1 = self.rule1(seat, adjacent_seats)
        state2 = self.rule2(seat, adjacent_seats, standup_treshold)
        new_state = state2 or state1
        if new_state:
            return Seat(x=seat.x, y=seat.y, state=new_state, changed=True)
        elif not new_state and seat.changed:
            return Seat(x=seat.x, y=seat.y, state=seat.state, changed=False)
        return seat


class Area:

    def __init__(self, config):
        self.seats = {}
        self.rules = Rules()
        self.config = config

        all_positions = sorted(self.seats.keys())
        self.size = all_positions[-1] if all_positions else (0, 0)

    def __str__(self):
        result = ''
        size = self.size
        for y in range(1, size[1] + 1):
            for x in range(1, size[0] + 1):
                result += self.seats[(x, y)].state
            result += '/n'
        return result

    @property
    def occupied_seats(self):
        return [seat.state for seat in self.seats.values()].count('#')

    def empty_area(self):
        self.seats = {}

    def add_seat(self, seat):
        self.seats[seat.position] = seat

    def reset_size(self):
        all_positions = sorted(self.seats.keys())
        self.size = all_positions[-1] if all_positions else (0, 0)

    def read_seats_from_file(self, filename):
        f = open(filename)
        for y, l in enumerate(f.readlines()):
            for x, ch in enumerate(l):
                if ch in '.L#':
                    seat = Seat(x + 1, y + 1, ch)
                    self.seats[seat.position] = seat
        self.reset_size()

    def get_next_seat(self, seat, direction):
        x = seat.x + DIRECTIONS[direction]['x']
        y = seat.y + DIRECTIONS[direction]['y']
        if x > 0 and x <= self.size[0] and y > 0 and y <= self.size[1]:
            seat = self.seats[(x, y)]
        else:
            return None

        if seat.state in 'L#':
            return seat
        elif seat.state == '.':
            return self.get_next_seat(seat, direction)

    def _get_adjacent_seats_extended(self, seat):
        results = []
        for direction in DIRECTIONS:
            result = self.get_next_seat(seat, direction)
            if result is not None:
                results.append(result)
        return results

    def _get_adjacent_seats_standard(self, seat):
        positions = seat.get_adjacent_positions()
        result = [self.seats.get(position, None) for position in positions]
        return filter(None, result)

    def get_adjacent_seats(self, seat):
        if self.config.look_beyond_dots:
            return self._get_adjacent_seats_extended(seat)
        return self._get_adjacent_seats_standard(seat)

    def apply_rules_on_seat(self, seat):
        adjacent_seats = self.get_adjacent_seats(seat)
        return self.rules.apply(
            seat,
            adjacent_seats,
            self.config.standup_treshold
        )

    def apply_rules(self):
        new_seats = list(map(self.apply_rules_on_seat, self.seats.values()))
        if self.new_seats_are_different(new_seats):
            self.empty_area()
            [self.add_seat(seat) for seat in new_seats]
            return True
        return False

    def apply_rules_in_loop(self, max_iterations=10):
        for _ in range(max_iterations):
            seats_different = self.apply_rules()
            if not seats_different:
                return self.occupied_seats
        return None

    def new_seats_are_different(self, new_seats):
        if any([seat.changed for seat in new_seats]):
            return True
        return False


if __name__ =='__main__':

    config1 = Config(standup_treshold=4, look_beyond_dots=False)
    config2 = Config(standup_treshold=5, look_beyond_dots=True)

    # Part 1
    area = Area(config1)
    area.read_seats_from_file('inputdata/day-11-1.txt')
    occupied_seats = area.apply_rules_in_loop(10)
    print(occupied_seats)

    area = Area(config1)
    area.read_seats_from_file('inputdata/day-11-2.txt')
    occupied_seats = area.apply_rules_in_loop(100)
    print(occupied_seats)

    # Part 2
    area = Area(config2)
    area.read_seats_from_file('inputdata/day-11-1.txt')
    occupied_seats = area.apply_rules_in_loop(10)
    print(occupied_seats)

    area = Area(config2)
    area.read_seats_from_file('inputdata/day-11-2.txt')
    occupied_seats = area.apply_rules_in_loop(100)
    print(occupied_seats)
