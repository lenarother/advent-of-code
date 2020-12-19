"""Day 6

https://adventofcode.com/2020/day/6

"""

def get_answers_sum(filename):
    return sum([
        len(set(group.replace('\n', '')))
        for group in open(filename).read().split('\n\n')
    ])


def get_common_answers_sum(filename):
    return sum([
        len(set.intersection(*map(set, filter(None, group.split('\n')))))
        for group in open(filename).read().split('\n\n')
    ])


if __name__ =='__main__':
    # Part 1
    result = get_answers_sum('inputdata/day-06-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = get_answers_sum('inputdata/day-06-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = get_common_answers_sum('inputdata/day-06-1.txt')
    print('Part 2 - Test set 1: ', result)

    result = get_common_answers_sum('inputdata/day-06-2.txt')
    print('Part 2 - Result: ', result)
