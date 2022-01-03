from docs.advent import Aoc
from docs.badge import get_badges


def write_readme(output_file):
    f = open(output_file, 'w')
    aoc = Aoc()
    badges = get_badges(aoc)
    f.write(f'{badges}{aoc}'.rstrip())
    f.close()


if __name__ == '__main__':
    write_readme('README.rst')
