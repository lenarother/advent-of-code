#! /usr/bin/env python
import os
import re
from datetime import datetime

import click
import requests
from cookiecutter.main import cookiecutter

TITLE = r'\d+\: (.+) ---'


def read_user_variable(var_name, default_value):
    # From: https://github.com/cookiecutter/cookiecutter/blob/master/cookiecutter/prompt.py
    return click.prompt(var_name, default=default_value)


def get_title(url, day):
    response = requests.get(url)
    if response.status_code == 200:
        search = re.findall(TITLE, response.text)
        if len(search) > 0:
            return f'Day {day}: {search[0]}'
    return 'title'


def get_output_dir(year):
    output_dir = os.path.abspath(
        os.path.join(
            os.getcwd(),
            f'adventofcode_{year}'
        )
    )
    if os.path.isdir(output_dir):
        return output_dir
    return '.'


today = datetime.today()
day = read_user_variable('day', today.day)
year = read_user_variable('year', today.year)
dirname = f'day_{str(day).zfill(2)}'
url = f'https://adventofcode.com/{year}/day/{day}'
title = get_title(url, day)
output_dir = read_user_variable('output_dir', get_output_dir(year))
cookiecutter_path = os.path.join(
    os.path.abspath(os.getcwd()),
    'template',
    'cookiecutter-aoc'
)


cookiecutter(
    cookiecutter_path,
    extra_context={
        '_day': day,
        '_year': year,
        '_dirname': dirname,
        '_title': title,
        '_url': url,
        '_aoc_cookiecutter_path': cookiecutter_path,
    },
    output_dir=output_dir
)