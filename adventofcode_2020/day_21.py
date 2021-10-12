"""Day 21: Allergen Assessment

https://adventofcode.com/2020/day/21

"""


def parse_input(filename):
    data = open(filename).read().strip().split('\n')

    line_data_dict = {}
    allergen_lines_dict = {}
    allergen_dict = {}

    for counter, line in enumerate(data):
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split()
        allergens = allergens.strip().replace(')', '').split(', ')
        line_data_dict[counter] = [ingredients, allergens]
        for allergen in allergens:
            allergen_dict.setdefault(allergen, None)
            allergen_lines_dict.setdefault(allergen, [])
            allergen_lines_dict[allergen].append(counter)

    return line_data_dict, allergen_lines_dict, allergen_dict


def refine_allergen_dict(line_data_dict, allergen_lines_dict, allergen_dict):
    for allergen in allergen_lines_dict:
        list_of_ingredient_lists = [
            line_data_dict[line][0]
            for line in allergen_lines_dict[allergen]
        ]
        common_ingredients = set.intersection(
            *[
                set(ingredient_list)
                for ingredient_list in list_of_ingredient_lists
            ]
        )
        if len(common_ingredients) == 1:
            allergen_dict[allergen] = list(common_ingredients)[0]

    return allergen_dict


def refine_line_data_dict(line_data_dict, allergen_dict, allergen_lines_dict):
    for allergen, ingredient in allergen_dict.items():
        if ingredient:
            for line in line_data_dict:
                if ingredient in line_data_dict[line][0]:
                    line_data_dict[line][0].remove(ingredient)
                if allergen in line_data_dict[line][1]:
                    line_data_dict[line][1].remove(allergen)
    return line_data_dict


def eliminate_allergens(line_data_dict, allergen_lines_dict, allergen_dict):
    if list(allergen_dict.values()).count(None) == 0:
        return allergen_dict, line_data_dict

    allergen_dict = refine_allergen_dict(
        line_data_dict,
        allergen_lines_dict,
        allergen_dict
    )
    line_data_dict = refine_line_data_dict(
        line_data_dict,
        allergen_dict,
        allergen_lines_dict
    )
    return eliminate_allergens(
        line_data_dict,
        allergen_lines_dict,
        allergen_dict
    )


def find_non_allergic_ingredient_count(filename):
    line_data_dict, allergen_lines_dict, allergen_dict = parse_input(filename)
    allergen_dict, line_data_dict = eliminate_allergens(
        line_data_dict,
        allergen_lines_dict,
        allergen_dict
    )
    return sum([len(v[0]) for v in line_data_dict.values()])


def find_canonical_dangerous_ingredient_list(filename):
    line_data_dict, allergen_lines_dict, allergen_dict = parse_input(filename)
    allergen_dict, line_data_dict = eliminate_allergens(
        line_data_dict,
        allergen_lines_dict,
        allergen_dict
    )
    allergen_ingredient_list = sorted(
        [(k, v) for k, v in allergen_dict.items()])
    return ','.join(x[1] for x in allergen_ingredient_list)


if __name__ == '__main__':

    # Part 1
    result = find_non_allergic_ingredient_count('inputdata/day-21-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = find_non_allergic_ingredient_count('inputdata/day-21-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = find_canonical_dangerous_ingredient_list('inputdata/day-21-1.txt')
    print('Part 2 - Test set 1: ', result)

    result = find_canonical_dangerous_ingredient_list('inputdata/day-21-2.txt')
    print('Part 2 - Result: ', result)
