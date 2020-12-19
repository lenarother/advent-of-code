"""Day 16

https://adventofcode.com/2020/day/16

"""

import itertools


def read_input(filename):
    """Parse input from file.

    Args:
        filename (str)

    Returns:
        rules (list): lines
        my_ticket (str)
        tickets (list): lines

    """
    data = open(filename).read().split('\n\n')
    rules = data[0].split('\n')
    my_ticket = data[1].split('\n')[1]
    tickets = data[2].strip().split('\n')[1:]
    return rules, my_ticket, tickets


def check_value(value, rules):
    """Check single value from ticket against given rules.

    Args:
        value (int): value to check
        rules (list): list of int-pairs e.g. [(1, 3), (7, 11) ...]

    Returns:
        int:
            0: if value is valid
            value: if value is invalid

    """
    for rule in rules:
        if (rule[0] <= value <=rule[1]):
            return 0
    return value


def check_ticket(ticket, rules):
    """Check if ticket is valid.

    Args:
        ticket (str)
        rules (list of int-pairs)

    Returns:
        int:
            0: if ticket is valid
            sum of invalide values: if ticket is invalid

    """
    result = 0
    ticket_vals = map(int, ticket.split(','))
    for val in ticket_vals:
        result += check_value(val, rules)
    return result


def collapse_rules(rules):
    """Minimise number of validation rules

    Merge rules if possible to get less ruless.

    Args:
        rules (list): int pairs

    Returns:
        list: int pairs

    """
    result = []
    current = rules[0]
    for rule in rules[1:]:
        if current[0] == rule[0] or current[1] >= rule[0]:
            current = [current[0], max(current[1], rule[1])]
        else:
            result.append(current)
            current = rule
    result.append(current)
    return result


def parse_rules_to_dict(rules):
    rules_dict = {}
    for l in rules:
        name, value = l.split(':')
        rule1, rule2 = value.strip().split(' or ')
        rules_dict.setdefault(name, [])
        rules_dict[name].append([int(x) for x in rule1.split('-')])
        rules_dict[name].append([int(x) for x in rule2.split('-')])
    return rules_dict


def parse_rules_to_list(rules):
    rules = parse_rules_to_dict(rules)
    rules = list(itertools.chain(*rules.values()))
    rules.sort()
    return collapse_rules(rules)


def check_column(column, rules_list):
    # Part 2
    for val in column:
        if check_value(val, rules_list) != 0:
            return False
    return True


def find_column_for_rule(columns_dict, rules_dict):
    # Part 2
    result = {}

    for rule in rules_dict:
        for k, v in columns_dict.items():
            if check_column(v, rules_dict[rule]):
                result.setdefault(rule, [])
                result[rule].append(k)

    return result


def get_valid_tickets(rules, tickets):
    # Part 2
    rules = parse_rules_to_list(rules)
    valid_tickets = []
    for ticket in tickets:
        if check_ticket(ticket, rules) == 0:
            valid_tickets.append(map(int, ticket.split(',')))

    return valid_tickets


def find_single_mapping(mappings):
    # Part 2
    max_len = max(len(x) for x in mappings.values())
    result = {}
    taken = []

    for counter in range(1, max_len + 1):
        for k in mappings:
            if len(mappings[k]) == counter:
                for id in mappings[k]:
                    if id not in taken:
                        result[k] = id
                        taken.append(id)
    return result


def multiply_invalid_values(filename):
    # Part 1 solution
    result = 0

    rules, _, tickets = read_input(filename)
    rules = parse_rules_to_list(rules)

    for ticket in tickets:
        result += check_ticket(ticket, rules)

    return result


def multiply_myticket_departure_fields(filename):
    rules, my_ticket, tickets = read_input(filename)

    valid_tickets = get_valid_tickets(rules, tickets)
    transposed_tickets = map(list, zip(*valid_tickets))
    columns_dict = {counter: column for counter, column in enumerate(transposed_tickets)}
    rules_dict = parse_rules_to_dict(rules)

    multiple_mapping = find_column_for_rule(columns_dict, rules_dict)
    mapping = find_single_mapping(multiple_mapping)

    result = 1
    my_ticket_values = [int(x) for x in my_ticket.split(',')]
    for field in mapping:
        if field.startswith('departure'):
            result = result * my_ticket_values[mapping[field]]

    return result


if __name__ =='__main__':

    # Part 1
    result = multiply_invalid_values('inputdata/day-16-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = multiply_invalid_values('inputdata/day-16-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = multiply_myticket_departure_fields('inputdata/day-16-2.txt')
    print('Part 2 - Result: ', result)
