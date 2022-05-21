"""Day 15: Science for Hungry People

https://adventofcode.com/2015/day/15

"""
import heapq
import math
import re

INGREDIENT = re.compile(
    r'\w+: capacity (-?\d+), durability (-?\d+), '
    r'flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
)


def parse(data):
    return [
        tuple(map(int, i))
        for i in INGREDIENT.findall(data)
    ]


def multiply_by_spoons(ingredient, spoons):
    return [spoons * i for i in ingredient]


def get_cookie(ingredients):
    cookie = [sum(i) for i in zip(*ingredients)]
    return [i if i > 0 else 0 for i in cookie]


def get_cookie_value(cookie):
    return math.prod(cookie[:-1])


def get_cookie_calories(cookie):
    return cookie[-1]


def get_all_spoon_values(ingredients):
    return {
        i: {
            s: multiply_by_spoons(i, s)
            for s in range(101)
        }
        for i in ingredients
    }


def cook(receipt, ingredients, spoons):
    ready_ingredients = [spoons[i][s] for s, i in zip(receipt, ingredients)]
    cookie = get_cookie(ready_ingredients)
    return get_cookie_value(cookie), get_cookie_calories(cookie)


def next_receipt(receipt):
    for i in range(len(receipt)):
        new_receipt = [x for x in receipt]
        new_receipt[i] += 1
        if new_receipt[i] > 100:
            continue
        yield new_receipt


def solve(data, calories=False):
    ingredients_list = parse(data)
    ingredients_dict = get_all_spoon_values(ingredients_list)

    receipts = []
    visited_receipts = set()
    result_with_calories = set()

    receipt = [1 for i in ingredients_list]
    cookie_value, cal = cook(receipt, ingredients_list, ingredients_dict)
    heapq.heappush(receipts, (cookie_value * -1, receipt, cal))

    while receipts:
        v, r, c = heapq.heappop(receipts)

        if sum(r) == 100:
            if calories is False:
                return abs(v)
            elif abs(c) == 500:
                result_with_calories.add(abs(v))

        for new_r in next_receipt(r):
            if tuple(new_r) not in visited_receipts:
                new_v, new_c = cook(new_r, ingredients_list, ingredients_dict)
                if calories is False:
                    heapq.heappush(receipts, (new_v * -1, new_r, new_c))
                elif new_c <= 500 and sum(new_r) <= 100:
                    heapq.heappush(receipts, (new_v * -1, new_r, new_c))
                visited_receipts.add(tuple(new_r))

    return max(result_with_calories)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, calories=True)
    print(f'Example2: {result}')
