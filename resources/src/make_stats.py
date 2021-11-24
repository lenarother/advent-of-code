import datetime
import re

import requests
from utils import get_board_id, get_cookie, get_user_id, read_config

STAT_URL = 'https://adventofcode.com/{year}/stats'
LIDERSHIP_BOARD = (
    'https://adventofcode.com/{year}/leaderboard/private/view/{board}.json'
)

STARS_1 = (
    r'<a href="/\d+/day/1"> 1  <span class="stats-both">\s*(\d+)</span>  '
    r'<span class="stats-firstonly">\s*(\d+)</span>'
)
STARS_50 = (
    r'<a href="/\d+/day/25">25  <span class="stats-both">\s*(\d+)</span>'
)


def get_stars(year):
    resp = requests.get(STAT_URL.format(year=year))
    stars_1 = sum(map(int, re.findall(STARS_1, resp.text)[0]))
    stars_50 = int(re.findall(STARS_50, resp.text)[0])
    return stars_1, stars_50


def get_my_stars(year):
    config = read_config()
    cookie = get_cookie(config)
    bord_id = get_board_id(config)
    user_id = get_user_id(config)
    board_url = LIDERSHIP_BOARD.format(year=year, board=bord_id)
    response = requests.post(
        board_url,
        cookies={'session': cookie}
    )
    try:
        response_json = response.json()
        return response_json['members'][user_id]['stars']
    except Exception:
        return ''


def get_year_record(year):
    stars_1, stars_50 = get_stars(year)
    my_stars = get_my_stars(year)
    ratio = round((stars_50 / stars_1) * 100)
    stars_1_str = '{:_}'.format(stars_1).rjust(10)
    stars_50_str = '{:_}'.format(stars_50).rjust(10)
    ratio_str = f'{ratio}%'.rjust(10)
    my_stars_str = str(my_stars).rjust(10)
    return (
        f' {year} | '
        f'{stars_1_str} | '
        f'{stars_50_str} | '
        f'{ratio_str} | '
        f'{my_stars_str}'
    )


def get_header():
    return (
        f' year | {"1 star".center(10)} | '
        f'{"50 stars".center(10)} | '
        f'{"ratio".center(10)} | '
        f'{"my stars".center(10)}'
    )


def get_line():
    return '-' * (6 + 1 + 12 + 1 + 12 + 1 + 12 + 1 + 12)


def print_stat():
    print()
    print(get_line())
    print(get_header())
    print(get_line())
    for y in range(2015, datetime.datetime.now().year):
        print(get_year_record(y))
    print(get_line())
    print()


if __name__ == '__main__':
    print_stat()
