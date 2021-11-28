import os
import urllib.parse

from docs.badges import get_badges
from docs.titles import get_titles
from docs.utils import build_url

AOC_URL = 'https://adventofcode.com/'
GITHUB_URL = (
    'https://github.com/lenarother/advent-of-code-solutions/blob/master'
)
PROJECT_DIR = os.path.join(
    os.path.dirname(__file__),
    '../..',
)


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


class AocDay:

    def __init__(self, name, event):
        self.name = name.replace('.py', '')
        self.event = event
        self.local_path = os.path.join(PROJECT_DIR, event.name, name)
        self.n = int(name.split('_')[1].lstrip('0').rstrip('.py'))
        self.aoc_link = urllib.parse.urljoin(
            self.event.aoc_link,
            'day',
            self.n,
        )
        self.solution_link = self.get_solution_link()
        self.test_link = self.get_test_link()
        self.title = self.get_title()

    def __repr__(self):
        rep = (
            f'* **Day {self.n}**: '
            f'{self.title} '
            f'[`problem <{self.aoc_link}>`_] '
            f'[`solution <{self.solution_link}>`_]'
        )
        if self.event.year != '2020':
            rep += f'[`test <{self.test_link}>`_]'
        return rep

    def get_solution_link(self):
        event_path = build_url((GITHUB_URL, '/', self.event.name))
        if self.event.year == '2020':
            return build_url((event_path, f'{self.name}.py'))
        return build_url((event_path, self.name, 'solution.py'))

    def get_test_link(self):
        if self.event.year == '2020':
            return None
        return build_url((
            GITHUB_URL,
            self.event.name,
            self.name,
            'test_solution.py',
        ))

    def get_title(self):
        return self.event.titles.get(int(self.n), 'Title')


class Aoc:

    def __init__(self):
        self.events = {}
        self.titles = get_titles()
        self.parse_events()

    def __iter__(self):
        for e in sorted(self.events, reverse=True):
            yield self.events[e]

    def __repr__(self):
        repr = """

Advent of code
==============

"""
        for event in self:
            repr += f'{event}\n'
        return repr

    def parse_events(self):
        for d in os.listdir(PROJECT_DIR):
            if d.startswith('adventofcode_'):
                event = AocEvent(d, self.titles)
                self.events[event.year] = event

    def get_events(self):
        return [self.events[e] for e in sorted(self.events, reverse=True)]


def write_readme(output_file):
    f = open(output_file, 'w')
    aoc = Aoc()
    badges = get_badges(aoc)
    f.write(f'{badges}{aoc}'.rstrip())
    f.close()


if __name__ == '__main__':
    write_readme('test-readme.rst')
