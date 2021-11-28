from datetime import datetime
from functools import reduce
from urllib.parse import urljoin

FIRST_YEAR = 2015


def build_url(parts):
    return reduce(urljoin, parts)


def aoc_years():
    today = datetime.today()
    next_year = (today.year + 1) if today.month == 12 else today.year
    for y in range(FIRST_YEAR, next_year + 1):
        yield y


def aoc_days(year):
    first_day = 1
    last_day = 25
    today = datetime.today()
    if year == today.year:
        last_day = today.day
    for d in range(first_day, last_day + 1):
        yield d
