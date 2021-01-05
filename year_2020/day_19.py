"""Day 19: Monster Messages

https://adventofcode.com/2020/day/19

"""

import copy


class Rule:

    def __init__(self, id, rule_type, parent=None):
        self.id = id
        self.rule_type = rule_type
        self.parent = parent
        self.children = []
        self.result = None
        self.value = None
        self.message_orig = None
        self.is_resursive = None

    def __repr__(self):
        return f'{self.id}-{self.rule_type}-{self.result}'


def parse_data(filename):
    rules, messages = open(filename).read().split('\n\n')

    rules_dict = {}
    rules = rules.strip().split('\n')
    for rule in rules:
        k, v = rule.split(':')
        k = int(k)
        v = v.strip()
        if '"' in v:
            v = v.replace('"', '')
        elif ' | ' in v:
            v = v.split(' | ')
            v = [list(map(int, x.split(' '))) for x in v]
        else:
            v = list(map(int, v.split(' ')))
        rules_dict[k] = v

    messages = messages.strip().split('\n')

    return rules_dict, messages


def parse_rule(rule, rules_dict, parent=None):
    data = rules_dict[rule]

    if isinstance(data[0], list):
        rule_type = 'or'
    elif isinstance(data[0], int):
        rule_type = 'and'
    else:
        rule_type = 'leaf'

    r = Rule(id=rule, rule_type=rule_type, parent=parent)

    if rule_type == 'leaf':
        r.value = data
        return r

    elif rule_type == 'and':
        for x in data:
            r.children.append(parse_rule(x, rules_dict, r))

    elif rule_type == 'or':
        chr1 = Rule(id=rule, rule_type='and', parent=r)
        chr2 = Rule(id=rule, rule_type='and', parent=r)

        for x in data[0]:
            chr1.children.append(parse_rule(x, rules_dict, chr1))
        for x in data[1]:
            chr2.children.append(parse_rule(x, rules_dict, chr2))

        r.children = [chr1, chr2]
    return r


def check_message(message, rule):
    if rule.message_orig is None:
        rule.message_orig = message

    if rule.parent is None and rule.result and len(message) == 0:
        return rule.result

    elif rule.parent is None and rule.result and len(message) > 0:
        return False

    elif rule.rule_type == 'leaf' and rule.result is None:
        if len(message) == 0:
            rule.result = False
            return check_message(message, rule.parent)
        if rule.value == message[0]:
            rule.result = True
            return check_message(message[1:], rule.parent)
        else:
            rule.result = False
            return check_message(message, rule.parent)

    elif rule.rule_type == 'and':
        for ch in rule.children:
            if ch.result is None:
                return check_message(message, ch)
            elif ch.result is False:
                rule.result = False
                if rule.parent:
                    return check_message(rule.message_orig, rule.parent)
                else:
                    return False
        if all([ch.result for ch in rule.children]):
            rule.result = True
            if rule.parent:
                return check_message(message, rule.parent)
            else:
                if len(message) == 0:
                    return True
                else:
                    return False

    elif rule.rule_type == 'or':
        if rule.children[0].result is None:
            return check_message(
                message, rule.children[0]
            )
        elif rule.children[0].result is False and rule.children[1].result is None:
            return check_message(message, rule.children[1])
        elif rule.children[0].result is False and rule.children[1].result is False:
            rule.result = False
            return check_message(rule.message_orig, rule.parent)

        if any([ch.result for ch in rule.children]):
            rule.result = True
            if rule.parent:
                return check_message(message, rule.parent)
            else:
                if len(message) == 0:
                    return True
                else:
                    return False


def check_messages(filename, rule):
    rules_dict, messages = parse_data(filename)
    rule = parse_rule(rule, rules_dict)

    result = 0
    for message in messages:
        new_rule = copy.deepcopy(rule)
        try:
            is_valid = check_message(message, new_rule)
            if is_valid:
                result += 1
        except RecursionError:
            print(message, 'RecursionError')
    return result


def check_messages_with_rule_substitution(filename):
    alternatives = [
        {8: [42], 11: [42, 31]},
        {8: [42], 11: [42, 42, 31, 31]},
        {8: [42], 11: [42, 42, 42, 31, 31, 31]},
        {8: [42], 11: [42, 42, 42, 42, 31, 31, 31, 31]},
        {8: [42], 11: [42, 42, 42, 42, 42, 31, 31, 31, 31, 31]},

        {8: [42, 42], 11: [42, 31]},
        {8: [42, 42], 11: [42, 42, 31, 31]},
        {8: [42, 42], 11: [42, 42, 42, 31, 31, 31]},
        {8: [42, 42], 11: [42, 42, 42, 42, 31, 31, 31, 31]},
        {8: [42, 42], 11: [42, 42, 42, 42, 42, 31, 31, 31, 31, 31]},

        {8: [42, 42, 42], 11: [42, 31]},
        {8: [42, 42, 42], 11: [42, 42, 31, 31]},
        {8: [42, 42, 42], 11: [42, 42, 42, 31, 31, 31]},
        {8: [42, 42, 42], 11: [42, 42, 42, 42, 31, 31, 31, 31]},
        {8: [42, 42, 42], 11: [42, 42, 42, 42, 42, 31, 31, 31, 31, 31]},

        {8: [42, 42, 42, 42], 11: [42, 31]},
        {8: [42, 42, 42, 42], 11: [42, 42, 31, 31]},
        {8: [42, 42, 42, 42], 11: [42, 42, 42, 31, 31, 31]},
        {8: [42, 42, 42, 42], 11: [42, 42, 42, 42, 31, 31, 31, 31]},
        {8: [42, 42, 42, 42], 11: [42, 42, 42, 42, 42, 31, 31, 31, 31, 31]},

        {8: [42, 42, 42, 42, 42], 11: [42, 31]},
        {8: [42, 42, 42, 42, 42], 11: [42, 42, 31, 31]},
        {8: [42, 42, 42, 42, 42], 11: [42, 42, 42, 31, 31, 31]},
        {8: [42, 42, 42, 42, 42], 11: [42, 42, 42, 42, 31, 31, 31, 31]},
        {8: [42, 42, 42, 42, 42], 11: [42, 42, 42, 42, 42, 31, 31, 31, 31, 31]},
    ]

    valid_messages = {}
    messages_with_recursion_error = {}

    rules_dict, messages = parse_data(filename)
    for message in messages:
        valid_messages[message] = False

    for alternative in alternatives:
        rules_dict.update(alternative)
        rule = parse_rule(0, rules_dict)

        for message, value in valid_messages.items():
            if value is False:
                new_rule = copy.deepcopy(rule)
                try:
                    valid_messages[message] = check_message(message, new_rule)
                except RecursionError:
                    messages_with_recursion_error[message] = True

    return (
        sum(list(valid_messages.values())) +
        sum(list(messages_with_recursion_error.values()))
    )


if __name__ == '__main__':

    # Part 1
    result = check_messages('inputdata/day-19-2.txt', 0)
    print('Part 1 - Result: ', result)

    # Part 2
    # Change to inputdata/day-19-2.txt for real solution, but it takes a while.
    result = check_messages_with_rule_substitution('inputdata/day-19-3.txt')
    print('Part 2 - Result: ', result)
