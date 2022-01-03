import os
from datetime import datetime

FIRST_YEAR = 2015
AOC_URL = 'https://adventofcode.com/'
GITHUB_URL = (
    'https://github.com/lenarother/advent-of-code/blob/master'
)
PROJECT_DIR = os.path.join(
    os.path.dirname(__file__),
    '../../..',
)


def build_url(parts):
    return '/'.join(parts).replace('//', '').replace('///', '')


def aoc_years():
    today = datetime.today()
    next_year = (today.year + 1) if today.month == 12 else today.year
    for y in range(FIRST_YEAR, next_year + 1):
        yield y


# TODO: Fix return current year days only if december
def aoc_days(year):
    first_day = 1
    last_day = 25
    today = datetime.today()
    if year == today.year:
        last_day = today.day
    for d in range(first_day, last_day + 1):
        yield d
