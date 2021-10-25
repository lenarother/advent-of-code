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
from functools import reduce

VALUE_BOT = r'value (\d+) goes to bot (\d+)'
BOT_GIVES = (
    r'bot (\d+) gives low to (bot|output) (\d+) '
    r'and high to (bot|output) (\d+)'
)


class Zooming:

    def __init__(self, instructions):
        self.bots = defaultdict(set)
        self.outputs = {}
        self.instructions = instructions
        self.parse_initial_values()

    def parse_initial_values(self):
        parsed = re.findall(VALUE_BOT, self.instructions)
        for value, bot in parsed:
            value, bot = map(int, (value, bot))
            self.bots[bot].add(value)

    def is_bot_complete(self, bot):
        return len(self.bots[bot]) == 2

    def parse_zooming_instruction(self, parsed_instruction):
        bot, dest_low, low, dest_high, high = parsed_instruction
        bot, low, high = map(int, (bot, low, high))
        if self.is_bot_complete(bot):
            for dest_type, dest, v in zip(
                    (dest_low, dest_high),
                    (low, high),
                    sorted(self.bots[bot])
            ):
                if dest_type == 'bot':
                    self.bots[dest].add(v)
                else:
                    self.outputs[dest] = v

    def parse_zooming(self):
        parsed = re.findall(BOT_GIVES, self.instructions)
        for inst in parsed:
            self.parse_zooming_instruction(inst)

    def cycle_bots(self):
        while True:
            yield self.parse_zooming()

    def find_bot_with_values(self, values):
        for bot, bot_values in self.bots.items():
            if bot_values == set(values):
                return bot

    def find_value_for_output(self, out):
        return self.outputs.get(out, None)

    def find_product(self, outputs_list):
        values = [self.find_value_for_output(i) for i in outputs_list]
        if all(values):
            return reduce(lambda a, b: a * b, values, 1)

    def solve_bot(self, values):
        result = None
        cycle = self.cycle_bots()
        while result is None:
            next(cycle)
            result = self.find_bot_with_values(values)
        return result

    def solve_outputs(self, outputs):
        result = None
        cycle = self.cycle_bots()
        while result is None:
            next(cycle)
            result = self.find_product(outputs)
        return result


def solve_bot(instructions, input_values):
    zooming = Zooming(instructions)
    return zooming.solve_bot(input_values)


def solve_outputs(instructions, expected_outputs):
    zooming = Zooming(instructions)
    return zooming.solve_outputs(expected_outputs)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result_bot = solve_bot(input_data, (17, 61))
    print(f'Example1: {result_bot}')

    input_data = open('input_data.txt').read()
    result_output = solve_outputs(input_data, (0, 1, 2))
    print(f'Example2: {result_output}')
