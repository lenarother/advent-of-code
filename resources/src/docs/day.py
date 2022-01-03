import os

from .utils import GITHUB_URL, PROJECT_DIR


class AocDay:

    def __init__(self, name, event):
        self.name = name.replace('.py', '')
        self.event = event
        self.local_path = os.path.join(PROJECT_DIR, event.name, name)
        self.n = int(name.split('_')[1].lstrip('0').rstrip('.py'))
        self.aoc_link = f'{self.event.aoc_link}/day/{self.n}'
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
        if self.event.year == '2020':
            return f'{GITHUB_URL}/{self.event.name}/{self.name}.py'
        return f'{GITHUB_URL}/{self.event.name}/{self.name}/solution.py'

    def get_test_link(self):
        if self.event.year == '2020':
            return None
        return f'{GITHUB_URL}/{self.event.name}/{self.name}/test_solution.py'

    def get_title(self):
        return self.event.titles.get(int(self.n), 'Title')
