"""Day 14: Reindeer Olympics

https://adventofcode.com/2015/day/14

"""
import re

REINDEER = re.compile(
    r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)'
)


class Reindeer:

    def __init__(self, name, speed, fly_t, rest_t):
        self.name = name
        self.speed = speed
        self.fly_t = fly_t
        self.rest_t = rest_t

        # Part 2
        self.current_dist = 0
        self.current_t = 0
        self.points = 0

    def __repr__(self):
        return f'<Reindeer {self.name}>'

    def move(self):
        cycle = self.fly_t + self.rest_t
        relative_t = self.current_t % cycle
        if relative_t < self.fly_t:
            self.current_dist += self.speed
        self.current_t += 1

    def calc_distance(self, t):
        # Part 1
        dist = (t // (self.fly_t + self.rest_t)) * self.speed * self.fly_t
        remaining_t = t % (self.fly_t + self.rest_t)
        if remaining_t < self.fly_t:
            dist += remaining_t * self.speed
        else:
            dist += self.fly_t * self.speed
        return dist


def parse(data):
    return [
        Reindeer(name, int(speed), int(fly_t), int(rest_t))
        for name, speed, fly_t, rest_t in REINDEER.findall(data)
    ]


def solve(data, t):
    reindeers = parse(data)
    results = [r.calc_distance(t) for r in reindeers]
    return max(results)


def solve2(data, t):
    reindeers = parse(data)

    while t:
        dist = []
        for r in reindeers:
            r.move()
            dist.append(r.current_dist)
        max_dist = max(dist)
        for r in reindeers:
            if r.current_dist == max_dist:
                r.points += 1
        t -= 1

    return max([r.points for r in reindeers])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, 2503)
    print(f'Example1: {result}')

    result = solve2(input_data, 2503)
    print(f'Example2: {result}')
