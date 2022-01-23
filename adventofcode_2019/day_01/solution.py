"""Day 1: The Tyranny of the Rocket Equation

https://adventofcode.com/2019/day/1

"""
import re


def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_entire_fuel(mass):
    fuel = 0
    while 1:
        mass = mass // 3 - 2
        if mass > 0:
            fuel += mass
        else:
            return fuel


def solve(data, fuel_function=calculate_fuel):
    return sum([fuel_function(int(i)) for i in re.findall(r'\d+\n', data)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, fuel_function=calculate_entire_fuel)
    print(f'Example1: {result}')
