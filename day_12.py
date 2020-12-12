"""Day 12

https://adventofcode.com/2020/day/12

"""

from day_base import get_inpit_list_from_file

TURNS = {
    'L': {
        'E': 'NWS',
        'W': 'SEN',
        'N': 'WSE',
        'S': 'ENW',
    },
    'R': {
        'E': 'SWN',
        'W': 'NES',
        'N': 'ESW',
        'S': 'WNE',
    }
}


class Ship:

    def __init__(self, data):
        self.direction = None
        self.waypoint = None
        self.position = {
            'E': 0,
            'W': 0,
            'N': 0,
            'S': 0,
        }
        if isinstance(data, str):
            self.direction = data
        elif isinstance(data, dict):
            self.waypoint = data

    def turn_waypoint(self, action, dist):
        new_waypoint = {}
        for direction, value in self.waypoint.items():
            new_key = self.get_direction(action, dist, direction)
            new_waypoint[new_key] = value
        self.waypoint = new_waypoint

    def move_with_waypoint(self, action, dist):
        if action in self.waypoint:
            self.waypoint[action] += dist
        elif action in 'LR':
            self.turn_waypoint(action, dist)
        elif action == 'F':
            for direction, val in self.waypoint.items():
                self.position[direction] += val * dist

    def move(self, action, dist):
        if action in self.position:
            self.position[action] += dist
        elif action == 'F':
            self.position[self.direction] += dist
        elif action in 'LR':
            new_direction = self.get_direction(action, dist, self.direction)
            self.direction = new_direction

    def get_direction(self, action, dist, current_direction):
        dist = dist % 360
        dist = dist / 90
        return TURNS[action][current_direction][int(dist - 1)]

    def get_manhattan_distance(self):
        ns = abs(self.position['N'] - self.position['S'])
        ew = abs(self.position['E'] - self.position['W'])
        return ns + ew

    def go(self, instruction_list):
        for inst in instruction_list:
            action = inst[0]
            dist = int(inst[1:])
            if self.waypoint:
                self.move_with_waypoint(action, dist)
            else:
                self.move(action, dist)
        return self.get_manhattan_distance()


if __name__ =='__main__':

    # Input
    input1 = get_inpit_list_from_file('inputdata/day-12-1.txt')
    input2 = get_inpit_list_from_file('inputdata/day-12-2.txt')

    # Part 1
    result = Ship('E').go(input1)
    print('Part 1 - Test set 1: ', result)

    result = Ship('E').go(input2)
    print('Part 1 - Test set 2: ', result)

    # Part 2
    result = Ship({'E': 10, 'W': 0, 'N': 1, 'S': 0}).go(input1)
    print('Part 2 - Test set 1: ', result)

    result = Ship({'E': 10, 'W': 0, 'N': 1, 'S': 0}).go(input2)
    print('Part 1 - Test set 2: ', result)
