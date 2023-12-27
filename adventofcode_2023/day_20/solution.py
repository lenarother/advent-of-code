"""Day 20: Pulse Propagation

https://adventofcode.com/2023/day/20

"""
import math
from collections import deque
from dataclasses import dataclass


@dataclass
class Module:
    name: str
    destinations: None | list[str]

    def broadcast(self, source, signal):
        # source name, signal (1 / 0), target name
        return [
            (self.name, signal, target)
            for target in self.destinations
        ]


@dataclass
class FlipFlopModule(Module):
    # Prefix  %
    state: int = 0  # off

    def __eq__(self, other):
        return self.state == other.state

    def broadcast(self, source, signal):
        if signal == 1:
            return
        elif signal == 0:
            self.state += 1
            self.state %= 2
            return [(self.name, self.state, i) for i in self.destinations]


@dataclass
class ConjunctionModule(Module):
    # Prefix  &
    # Default memory is low pulse for each input
    memory: dict

    def __eq__(self, other):
        return self.memory == other.memory

    def broadcast(self, source, signal):
        self.memory[source] = signal
        signal = (int(all(self.memory.values())) + 1) % 2
        return [(self.name, signal, i) for i in self.destinations]


@dataclass
class BroadcasterModule(Module):

    def __eq__(self, other):
        return True


def parse_module(line):
    name, destinations = line.split(' -> ')
    destinations = destinations.strip().split(', ')

    if name == 'broadcaster':
        return BroadcasterModule(
            name=name,
            destinations=destinations,
        )
    elif name.startswith('%'):
        return FlipFlopModule(
            name=name[1:],
            destinations=destinations,
        )
    elif name.startswith('&'):
        return ConjunctionModule(
            name=name[1:],
            destinations=destinations,
            memory={}
        )


def update_memory(modules):
    conjunctions = [
        m.name for m in modules.values()
        if isinstance(m, ConjunctionModule)
    ]
    for name, module in modules.items():
        cons = set(module.destinations).intersection(conjunctions)
        if len(cons) > 0:
            for con in cons:
                modules[con].memory[name] = 0


def parse_modules(data):
    modules = {
        module.name: module
        for module in
        [parse_module(line) for line in data.strip().split('\n')]
    }
    update_memory(modules)
    return modules


class System:

    def __init__(self, data):
        self.modules = parse_modules(data)
        self.signals = deque([])
        self.signal_cunt = 0
        self.high_count = 0

    def run(self):
        x = 1000
        while x:
            x -= 1
            self.signals.append(('button', 0, 'broadcaster'))
            while self.signals:
                source, signal, destination = self.signals.popleft()
                self.signal_cunt += 1
                self.high_count += signal

                module = self.modules.get(destination)
                if module:
                    new_signals = module.broadcast(source, signal)
                    if new_signals:
                        self.signals += new_signals
        return self.get_result()

    def get_result(self):
        low_count = self.signal_cunt - self.high_count
        return low_count * self.high_count


class System2:

    def __init__(self, data):
        self.modules = parse_modules(data)
        self.signals = deque([])

    def run(self):
        x = 0
        interesting_pulses = set()

        while len(interesting_pulses) < 4:
            x += 1
            self.signals.append(('button', 0, 'broadcaster'))
            while self.signals:
                source, signal, destination = self.signals.popleft()
                module = self.modules.get(destination)
                if module:
                    if module.name == 'gf' and sum(module.memory.values()):
                        interesting_pulses.add(x)
                    new_signals = module.broadcast(source, signal)
                    if new_signals:
                        self.signals += new_signals

        return math.lcm(*interesting_pulses)


def solve(data):
    system = System(data)
    return system.run()


def solve_2(data):
    system = System2(data)
    return system.run()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example1: {result}')
