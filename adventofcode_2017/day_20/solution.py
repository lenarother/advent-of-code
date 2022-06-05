"""Day 20: Particle Swarm

https://adventofcode.com/2017/day/20

"""
import re
from collections import defaultdict

PARTICLE = re.compile(r'p=<(.*)>, v=<(.*)>, a=<(.*)>')


def parse(data):
    particles = {}
    for i, item in enumerate(data.strip().split('\n')):
        p, v, a = PARTICLE.findall(item)[0]
        particles[i] = {
            'p': list(map(int, p.split(','))),
            'v': list(map(int, v.split(','))),
            'a': list(map(int, a.split(','))),
        }
    return particles


def update_particles(particle_dict):
    for p in particle_dict.values():
        p['v'] = list(map(lambda a, b: a + b, p['v'], p['a']))
        p['p'] = list(map(lambda a, b: a + b, p['p'], p['v']))
    return particle_dict


def calculate_distance(particle_dict):
    return {
        k: sum(list(map(abs, v['p'])))
        for k, v in particle_dict.items()
    }


def remove_collisions(particle_dict):
    p_dict = defaultdict(list)
    for k, v in particle_dict.items():
        p_dict[tuple(v['p'])].append(k)
    for k, v in p_dict.items():
        if len(v) > 1:
            for i in v:
                particle_dict.pop(i)
    return particle_dict


def solve(data, n=1000):
    particle_dict = parse(data)
    while n:
        update_particles(particle_dict)
        n -= 1
    distances = calculate_distance(particle_dict)
    return min(distances, key=distances.get)


def solve2(data, n=1000):
    particle_dict = parse(data)
    while n:
        update_particles(particle_dict)
        remove_collisions(particle_dict)
        n -= 1
    return len(particle_dict)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
