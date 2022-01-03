import os

from .event import AocEvent
from .title import get_titles
from .utils import PROJECT_DIR


class Aoc:

    def __init__(self):
        self.events = {}
        self.titles = get_titles()
        self.parse_events()

    def __iter__(self):
        for e in sorted(self.events, reverse=True):
            yield self.events[e]

    def __repr__(self):
        rep = """

Advent of code
==============

"""
        for event in self:
            rep += f'{event}\n'
        return rep

    def parse_events(self):
        for d in os.listdir(PROJECT_DIR):
            if d.startswith('adventofcode_'):
                event = AocEvent(d, self.titles)
                self.events[event.year] = event

    def get_events(self):
        return [self.events[e] for e in sorted(self.events, reverse=True)]
