import configparser
import os

CONF_PATH = os.path.join(
    os.path.dirname(__file__),
    '../..',
    'template',
    '.aoc.conf'
)


def read_config(config_path=CONF_PATH):
    cfg = configparser.ConfigParser()
    if os.path.isfile(config_path):
        cfg.read(config_path)
        return cfg


def get_cookie(config):
    if config.has_option('AOC', 'cookie'):
        return config.get('AOC', 'cookie')


def get_user_id(config):
    if config.has_option('AOC', 'userid'):
        return config.get('AOC', 'userid')


def get_board_id(config):
    if config.has_option('AOC', 'boardid'):
        return config.get('AOC', 'boardid')
