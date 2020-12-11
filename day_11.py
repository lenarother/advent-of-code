import pprint
from operator import itemgetter


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

    def rule2(self, seat, adjacent_seats):
        """Occupied -> Empty

        If a seat is occupied (#) and four or more seats adjacent to it are
        also occupied, the seat becomes empty.

        """
        if seat.state != '#' or sum(map(bool, adjacent_seats)) < 4:
            return None
        return 'L'

    def apply(self, seat, adjacent_seats):
        state1 = self.rule1(seat, adjacent_seats)
        state2 = self.rule2(seat, adjacent_seats)
        new_state = state2 or state1
        if new_state:
            return Seat(x=seat.x, y=seat.y, state=new_state, changed=True)
        elif not new_state and seat.changed:
            return Seat(x=seat.x, y=seat.y, state=seat.state, changed=False)
        return seat


class Area:

    def __init__(self):
        self.seats = {}
        self.rules = Rules()

    def __str__(self):
        result = ''
        size = self.size
        for y in range(1, size[1] + 1):
            for x in range(1, size[0] + 1):
                result += self.seats[(x, y)].state
            result += '/n'
        return result

    def empty_area(self):
        self.seats = {}

    def add_seat(self, seat):
        self.seats[seat.position] = seat

    @property
    def size(self):
        all_positions = sorted(self.seats.keys())
        return all_positions[-1]

    def read_seats_from_file(self, filename):
        f = open(filename)
        for y, l in enumerate(f.readlines()):
            for x, ch in enumerate(l):
                if ch in '.L#':
                    seat = Seat(x + 1, y + 1, ch)
                    self.seats[seat.position] = seat

    def get_adjacent_seats(self, seat):
        positions = seat.get_adjacent_positions()
        result = [self.seats.get(position, None) for position in positions]
        return filter(None, result)

    def apply_rules_on_seat(self, seat):
        adjacent_seats = self.get_adjacent_seats(seat)
        return self.rules.apply(seat, adjacent_seats)

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

    @property
    def occupied_seats(self):
        return [seat.state for seat in self.seats.values()].count('#')

    def new_seats_are_different(self, new_seats):
        if any([seat.changed for seat in new_seats]):
            return True
        return False


if __name__ =='__main__':

    # Part 1
    area = Area()
    area.read_seats_from_file('inputdata/day-11-1.txt')
    occupied_seats = area.apply_rules_in_loop(10)
    print(occupied_seats)

    area = Area()
    area.read_seats_from_file('inputdata/day-11-2.txt')
    occupied_seats = area.apply_rules_in_loop(100)
    print(occupied_seats)
