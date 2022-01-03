from abc import ABCMeta

BADGE_URL = 'https://img.shields.io/badge/'


class AbstractBadge(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.image_link = None
        self.target_link = None
        self.alt = None

    def __repr__(self):
        return f"""
.. {self.name} image:: {self.image_link}
   :target: {self.target_link}
   :alt: {self.alt}
"""


class AocBadge(AbstractBadge):

    def __init__(self, event):
        super().__init__()
        self.name = f'|AoC {event.year}|'
        self.alt = self.name
        self.image_link = (
            f'{BADGE_URL}{event.year}-{len(event) * 2}-yellow.svg'
        )
        self.target_link = event.aoc_link


class TestBadge(AbstractBadge):

    def __init__(self):
        super().__init__()
        self.name = '|AoC Test|'
        self.alt = self.name
        self.image_link = (
            'https://github.com/lenarother/advent-of-code/workflows'
            '/Test/badge.svg?branch=master'
        )
        self.target_link = (
            'https://github.com/lenarother/advent-of-code/'
            'actions?workflow=Test'
        )


class Badges:

    def __init__(self, aoc):
        self.badges = []
        self.collect_badges(aoc)

    def __repr__(self):
        rep = f"""{self.get_header()}
"""
        for b in self.badges:
            rep += f'{b}'
        return rep

    def get_header(self):
        return ' '.join(b.name for b in self.badges)

    def collect_badges(self, aoc):
        self.badges.append(TestBadge())
        for event in aoc:
            self.badges.append(AocBadge(event))


def get_badges(aoc):
    return Badges(aoc)
