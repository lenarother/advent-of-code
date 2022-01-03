import os
import urllib.parse

from .day import AocDay
from .utils import AOC_URL, PROJECT_DIR


class AocEvent:

    def __init__(self, name, titles=None):
        self.name = name
        self.year = name.split('_')[1]
        self.local_path = os.path.join(PROJECT_DIR, name)
        self.aoc_link = urllib.parse.urljoin(AOC_URL, self.year)
        self.days = {}
        self.titles = titles.get(int(self.year), {})
        self.parse_days()

    def __repr__(self):
        repr = f"""
Advent of Code {self.year}
-------------------

{self.aoc_link}

""".lstrip()
        for day in self:
            repr += f'{day}\n'
        repr += '\n'
        return repr

    def __len__(self):
        return len(self.days)

    def __iter__(self):
        for d in sorted(self.days):
            yield self.days[d]

    def parse_days(self):
        for d in os.listdir(self.local_path):
            if d.startswith('day_'):
                day = AocDay(d, self)
                self.days[day.n] = day
