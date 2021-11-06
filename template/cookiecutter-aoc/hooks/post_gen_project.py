import os
import configparser
import requests

CONFIG_FILE = '.aoc.conf'
CONFIG_SECTION = 'AOC'
CONFIG_COOKIE = 'cookie'

url = '{{ cookiecutter._url }}'
cookiecutter_path = '{{ cookiecutter._aoc_cookiecutter_path }}'


def read_config(cookiecutter_path):
    config_path = os.path.join(
        os.path.dirname(cookiecutter_path),
        CONFIG_FILE,
    )
    cfg = configparser.ConfigParser()
    if os.path.isfile(config_path):
        cfg.read(config_path)
        return cfg


def get_cookie(config):
    if config.has_option(CONFIG_SECTION, CONFIG_COOKIE):
        return config.get(CONFIG_SECTION, CONFIG_COOKIE)


def get_input(url, cookie):
    url = os.path.join(url, 'input')
    cookies = {'session': cookie}
    response = requests.post(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    return ''


def write_input(input_data):
    file_path = os.path.join(os.getcwd(), 'input_data.txt')
    f = open(file_path, 'w')
    f.write(input_data)
    f.close()


def main(url, cookiecutter_path):
    input_data = ''
    config = read_config(cookiecutter_path)
    if config:
        cookie = get_cookie(config)
        input_data = get_input(url, cookie)
    write_input(input_data)


main(url, cookiecutter_path)
