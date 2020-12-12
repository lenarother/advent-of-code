"""Day 2

https://adventofcode.com/2020/day/2

"""

from day_base import get_input_list_from_file


def parse_input(line):
    data = line.split()
    min_num = data[0].split('-')[0]
    min_num, max_num = data[0].split('-')
    min_num = int(min_num)
    max_num = int(max_num)
    letter = data[1].replace(':', '')
    password = data[2]
    return letter, min_num, max_num, password


def check_password(letter, min_num, max_num, password):
    letter_count = password.count(letter)
    return letter_count >= min_num and letter_count <= max_num


def check_password_2(letter, pos1, pos2, password):
    first_check = (len(password) >= pos1) and (password[pos1 - 1] == letter)
    second_check = (len(password) >= pos2) and (password[pos2 - 1] == letter)
    return first_check != second_check


def check_passwords(input, validation_func):
    valid_passwords_count = 0
    for line in input:
        valid_passwords_count += validation_func(*parse_input(line))
    return valid_passwords_count


if __name__ =='__main__':

    # Input
    input1 = get_input_list_from_file('inputdata/day-2-1.txt')
    input2 = get_input_list_from_file('inputdata/day-2-2.txt')

    # Part 1
    result = check_passwords(input1, check_password)
    print('Part 1 - Test set 1: ', result)

    result = check_passwords(input2, check_password)
    print('Part 1 - Result: ', result)

    # Part 2
    result = check_passwords(input1, check_password_2)
    print('Part 2 - Test set 1: ', result)

    result = check_passwords(input2, check_password_2)
    print('Part 2 - Result: ', result)
