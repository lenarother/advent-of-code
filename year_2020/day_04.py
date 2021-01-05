"""Day 4: Passport Processing

https://adventofcode.com/2020/day/4

"""

import re

PASS_REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
PASS_OPTIONAL_KEYS = ['cid']


def check_pass(pass_data):
    if len(pass_data) == 7:
        return set(PASS_REQUIRED_KEYS) == set(pass_data.keys())
    elif len(pass_data) == 8:
        return set(PASS_REQUIRED_KEYS + PASS_OPTIONAL_KEYS) == set(pass_data.keys())
    return False

def _check_date(val, dmin, dmax):
    return len(val) == 4 and val.isdigit() and (dmin <= int(val) <= dmax)

def _check_height(val):
    if len(val) < 4:
        return False
    hgt_val, hgt_unit = val[:-2], val[-2:]
    if not (hgt_unit in ['cm', 'in'] and hgt_val.isdigit()):
        return False
    if not (hgt_unit == 'cm' and (150 <= int(hgt_val) <= 193)):
        if not (hgt_unit == 'in' and (59 <= int(hgt_val) <= 76)):
            return False
    return True

def check_pass_details(pass_data):
    if not _check_date(pass_data['byr'], 1920, 2002):
        return False

    if not _check_date(pass_data['iyr'], 2010, 2020):
       return False

    if not _check_date(pass_data['eyr'], 2020, 2030):
        return False

    if not _check_height(pass_data['hgt']):
        return False

    if not re.search(r'^#([0-9a-f]{6})$', pass_data['hcl']):
        return False

    if not re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', pass_data['ecl']):
        return False

    if not re.search(r'^(\d){9}$', pass_data['pid']):
        return False

    return True


def check_data(filename, check_details=False):
    parsed_data = []
    valid_data = 0
    data = open(filename).read()
    data = data.split('\n\n')
    for item in data:
        pass_data = {}
        item = item.replace('\n', ' ').split()
        item_data = {}
        for i in item:
            k, v = i.split(':')
            item_data[k] = v
        parsed_data.append(item_data)
        check = check_pass(item_data)
        if check and check_details:
            check = check_pass_details(item_data)
        valid_data += check
    return valid_data


if __name__ =='__main__':

    # Part 1
    result = check_data('inputdata/day-04-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = check_data('inputdata/day-04-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = check_data('inputdata/day-04-1.txt', True)
    print('Part 2 - Test set 1: ', result)

    result = check_data('inputdata/day-04-2.txt', True)
    print('Part 2 - Result: ', result)
