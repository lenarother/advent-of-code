"""Day 7: Handy Haversacks

https://adventofcode.com/2020/day/7

"""


def parse_bag(bag, as_dict=False, as_tuple=False):
    k, v = bag.split(' bags contain ')
    if 'no other bags' in v:
        v = [] if not as_dict else {}
    else:
        v = v.split(',')
        v = [x.split() for x in v]
        if as_tuple:
            v = [(f'{x[1]} {x[2]}', int(x[0].strip())) for x in v]
        elif as_dict:
            v = {f'{x[1]} {x[2]}': int(x[0].strip()) for x in v}
        else:
            v = [f'{x[1]} {x[2]}' for x in v]
    return k, v


def parse_bags(filename, as_dict=False, as_tuple=False):
    result = {}
    for line in open(filename).read().strip().split('\n'):
        k, v = parse_bag(line, as_dict, as_tuple)
        result[k] = v
    return result


def reverse_bags(bags):
    """Part 1: Change parent - children dict -> child - parents dict."""
    result = {}
    for k, v in bags.items():
        for bag in v:
            result.setdefault(bag, [])
            result[bag].append(k)
    return result


def get_possible_parents(bag, reversed_bags, parents=None, has_new=None):
    # Part 1
    if parents is None:
        return get_possible_parents(
            bag,
            reversed_bags,
            reversed_bags[bag],
            True
        )

    if has_new is False:
        return len(set(parents))

    new_parents = []
    for parent in parents:
        if parent in reversed_bags:
            new_parents += reversed_bags[parent]

    has_new = False
    for bag in new_parents:
        if bag not in parents:
            parents.append(bag)
            has_new = True

    return get_possible_parents(bag, reversed_bags, parents, has_new)


def get_shiny_gold_bag_parents(filename):
    # Part 1
    bags = parse_bags(filename)
    reversed_bags = reverse_bags(bags)
    return get_possible_parents('shiny gold', reversed_bags)


def can_exchange(bag, bags_dict):
    # Part 2
    if bag[0] in bags_dict and len(bags_dict[bag[0]]) > 0:
        return True
    return False


def get_possible_children(bags_list, bags_dict, counter=0):
    new_bags = []
    for ch in bags_list:
        if can_exchange(ch, bags_dict):
            counter += ch[1]
            for n in bags_dict[ch[0]]:
                new_bags.append((n[0], n[1] * ch[1]))
        else:
            new_bags.append(ch)

    for bag in new_bags:
        if can_exchange(bag, bags_dict):
            return get_possible_children(new_bags, bags_dict, counter)

    for ch in new_bags:
        counter += ch[1]

    return counter - 1


def get_shiny_gold_bag_children(filename):
    # Part 2
    bags = parse_bags(filename, as_tuple=True)
    return get_possible_children([('shiny gold', 1)], bags)


if __name__ == '__main__':
    # Part 1
    result = get_shiny_gold_bag_parents('inputdata/day-07-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = get_shiny_gold_bag_parents('inputdata/day-07-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = get_shiny_gold_bag_children('inputdata/day-07-1.txt')
    print('Part 2 - Test set 1: ', result)

    result = get_shiny_gold_bag_children('inputdata/day-07-2.txt')
    print('Part 2 - Result: ', result)
