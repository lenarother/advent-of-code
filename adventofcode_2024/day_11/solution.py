"""Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11

"""

def apply_rule(n):
    if n == '0':
        return ['1']
    elif len(n) % 2 == 0:
        n_len = int(len(n) / 2)
        return [str(int(n[:n_len])), str(int(n[n_len:]))]
    else:
        return [str(int(n) * 2024)]



def solve_n(n, i, cache):
    if (n, i) in cache:
        return cache[(n, i)]

    nums = [n]
    while i:
        new_nums = []
        for x in nums:
            new_nums += apply_rule(x)
        i -= 1
        nums = new_nums

    len_nums = len(nums)
    cache[(n, i)] = len_nums
    return len_nums, nums


def solve_list(input_list, iterations, cache):
    result = 0
    new_nums = []
    for num in input_list:
        if (num, iterations) in cache:
            #print("Reading from cache")
            x, y = cache[(num, iterations)]
        else:
            x, y = solve_n(num, iterations, cache)
        result += x
        new_nums += y
        cache[(num, iterations)] = x, y
    return result, new_nums



def solve(data, iterations=75):
    cache = dict()
    input_list = [i for i in data.strip().split()]
    #result = 0
    #for i in input_list:
    #    x, y = solve_n(i, iterations, cache)
    #    result += x
    #return result


    foo = 7
    while foo:
        # print(foo)
        print("FOOOOO", foo)
        x, y = solve_list(input_list, 10, cache)
        input_list = y
        foo -= 1
    return len(input_list)




if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
