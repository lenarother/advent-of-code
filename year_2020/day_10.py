"""Day 10: Adapter Array

https://adventofcode.com/2020/day/10

"""

import itertools

input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
input2 = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11,
    1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
]
input3 = [
    71, 30, 134, 33, 51, 115, 122, 38, 61, 103, 21, 12, 44, 129, 29, 89, 54,
    83, 96, 91, 133, 102, 99, 52, 144, 82, 22, 68, 7, 15, 93, 125, 14, 92, 1,
    146, 67, 132, 114, 59, 72, 107, 34, 119, 136, 60, 20, 53, 8, 46, 55, 26,
    126, 77, 65, 78, 13, 108, 142, 27, 75, 110, 90, 35, 143, 86, 116, 79, 48,
    113, 101, 2, 123, 58, 19, 76, 16, 66, 135, 64, 28, 9, 6, 100, 124, 47, 109,
    23, 139, 145, 5, 45, 106, 41,
]

# Part 2 helper
exchange_chains = {
    1: ['1'],
    2: ['11', '2'],
    3: ['111', '12', '3'],
}

# Part 2 helper
permutation_count = {}


def get_differences_array(input):
    """Part 1: Sort list and calculate differences betwen n and n+1 element.

    Args:
        input: list (not sorted).

    Returns:
        dict: k -> difference betwen n and n+1, v -> num of occurences.

    """
    data = [0] + sorted(input) + [max(input) + 3]
    result = {}
    data_len = len(data)
    for count, val in enumerate(data):
        if count < data_len - 1:
            num = data[count + 1] - val
            result.setdefault(num, 0)
            result[num] += 1
    return result


def get_1_chains_lengths(input):
    """Part 2: Sort list and get lengths of sublists where el[n+1] - el[n] = 1.

    Args:
        input: list (not sorted).

    Returns:
        dict: k -> sublist length, v -> num of occurences.

    """
    data = [0] + sorted(input) + [max(input) + 3]
    result = {}
    data_len = len(data)
    counter = 0
    for count, val in enumerate(data):
        if count < data_len - 1:
            num = data[count + 1] - val
            if num == 1:
                counter += 1
            elif num == 3:
                result.setdefault(counter, 0)
                result[counter] += 1
                counter = 0
    return result


def get_possible_exchange_chains(num):
    """Part 2: Check which elements can be omitted.

    Given length of list with elements increase by 1 calculates
    chains (as str) that show how many elements can be removed
    from such a list to not exceed difference of 3 between adjacent elements.

    Args:
        num (int): length of list with elements increase by 1 (list1).

    Returns:
        list of chains (str). E.g. ['1111', '112', '13', '22']

    """
    if num in exchange_chains:  # use a global dict to reuse results
        return exchange_chains[num]
    num3 = num - 3
    num2 = num - 2
    list2 = get_possible_exchange_chains(num2)
    list3 = get_possible_exchange_chains(num3)
    list1_result = ['1' * num]
    list2_result = [''.join(sorted(x + '2')) for x in list2]
    list3_result = [''.join(sorted(x + '3')) for x in list3]
    list_result = list(set(list1_result + list2_result + list3_result))
    exchange_chains[num] = list_result
    return list_result


def get_chain_permutation_count(chain):
    """Part 2: Calculate number of permutations for omitted elements chain.

    Args:
        chain (str): e.g. '112'.

    Returns:
        number of permutation without repetition.

    """
    if chain in permutation_count:  # use a global dict to reuse results
        return permutation_count[chain]
    perms = len(set(itertools.permutations(chain)))
    permutation_count[chain] = perms
    return perms


def get_chains_num_from_input(input):
    """Part 2: Calculate number of possible chains.

    Given a list calculate the number of such chains where the difference
    between the adjacent elements is not greater than 3.

    Args:
        input: list (not sorted).

    Returns:
        number of possible chains.

    """
    result = 1
    chains = get_1_chains_lengths(input)
    for chain in chains:
        if chain > 1:
            exchange_chains = get_possible_exchange_chains(chain)
            permutations = 0
            for exchange_chain in exchange_chains:
                permutations += get_chain_permutation_count(exchange_chain)
            result = result * (permutations**chains[chain])
    return result


if __name__ =='__main__':

    # Part 1
    result_dict = get_differences_array(input1)
    result = result_dict[1] * result_dict[3]
    print('Part 1 - Test set 1: ', result)

    result_dict = get_differences_array(input2)
    result = result_dict[1] * result_dict[3]
    print('Part 1 - Test set 2: ', result)

    result_dict = get_differences_array(input3)
    result = result_dict[1] * result_dict[3]
    print('Part 1 - Result: ', result)


    # Part 2
    result = get_chains_num_from_input(input1)
    print('Part 2 - Test set 1: ', result)

    result = get_chains_num_from_input(input2)
    print('Part 2 - Test set 2: ', result)

    result = get_chains_num_from_input(input3)
    print('Part 2 - Result: ', result)
