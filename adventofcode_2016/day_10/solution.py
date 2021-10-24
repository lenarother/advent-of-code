""""Day 10: Balance Bots"

https://adventofcode.com/2016/day/10

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

Initially, bot 1 starts with a value-3 chip,
and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2)
to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips;
it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips;
it puts the 3 in output 2 and the 5 in output 0.

What is the number of the bot that is responsible
for comparing value-61 microchips with value-17 microchips?
"""
import re
from collections import defaultdict

VALUE_BOT = r'value (\d+) goes to bot (\d+)'
BOT_GIVES = (
    r'bot (\d+) gives low to (bot|output) (\d+) '
    r'and high to (bot|output) (\d+)'
)


def parse_instructions(instructions, bots):
    parsed = re.findall(VALUE_BOT, instructions)
    for value, bot in parsed:
        value, bot = map(int, (value, bot))
        bots[bot].add(value)

    parsed = re.findall(BOT_GIVES, instructions)
    for bot, dest_low, low, dest_high, high in parsed:
        bot, low, high = map(int, (bot, low, high))
        if dest_low == 'bot' and len(bots[bot]) == 2:
            bots[low].add(min(bots[bot]))
        if dest_high == 'bot' and len(bots[bot]) == 2:
            bots[high].add(max(bots[bot]))

    return bots


def solve(instructions, input_values):
    input_values = set(input_values)
    bots = defaultdict(set)
    result = None

    while result is None:
        bots = parse_instructions(instructions, bots)
        for bot, bot_values in bots.items():
            if bot_values == input_values:
                result = bot

    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    solution = solve(input_data, (17, 61))
    print(f'Example1: {solution}')
