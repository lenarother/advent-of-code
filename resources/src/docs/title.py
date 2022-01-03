import os
import re
from os.path import join

import requests

from .utils import aoc_days, aoc_years

AOC_DAY_URL = 'https://adventofcode.com/{year}/day/{day}'
LOCAL_TITLES_PATH = join(os.path.dirname(__file__), 'aoc_titles.txt')
TITLE = r'\d+\: (.+) ---'
SEPARATOR = '::'


def get_title_from_aoc(year, day):
    url = AOC_DAY_URL.format(year=year, day=day)
    response = requests.get(url)
    if response.status_code == 200:
        search = re.findall(TITLE, response.text)
        if len(search) > 0:
            return f'{search[0]}'


def scrape_aoc_titles():
    return {
        y: {
            d: get_title_from_aoc(y, d)
            for d in aoc_days(y)
        }
        for y in aoc_years()

    }


def read_aoc_titles_from_file():
    result = {}

    if not os.path.isfile(LOCAL_TITLES_PATH):
        return result

    for t in open(LOCAL_TITLES_PATH).read().strip().split('\n'):
        y, d, title = t.strip().split(SEPARATOR)
        result.setdefault(int(y), {})[int(d)] = title

    return result


def get_aoc_titles(clean=False):
    if clean:
        return scrape_aoc_titles()
    titles = read_aoc_titles_from_file()
    for y in aoc_years():
        for d in aoc_days(y):
            if not titles.get(y, {}).get(d, None):
                titles.setdefault(y, {})[d] = get_title_from_aoc(y, d)
    return titles


def write_titles(titles):
    f = open(LOCAL_TITLES_PATH, 'w')
    for y in aoc_years():
        for d in aoc_days(y):
            t = titles.get(y, {}).get(d, '')
            record = f'{y}{SEPARATOR}{d}{SEPARATOR}{t}\n'
            f.write(record)
    f.close()


def get_titles():
    titles = get_aoc_titles()
    write_titles(titles)
    return titles


if __name__ == '__main__':
    get_titles()
