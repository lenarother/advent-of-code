"""Day 18: Duet

https://adventofcode.com/2017/day/18

"""
import re
from collections import defaultdict, deque

INSTRUCTION_SET = re.compile(r'(\w\w\w) (\w)\s?(-?)(\d+|\w?)')


def get_val(val, sign, register):
    if not val:
        return 0
    if val.isnumeric():
        return int(val) if not sign else -1 * int(val)
    return register.get(val, 0)


def parse_instructions(instructions):
    return {
        k: v for k, v
        in enumerate(instructions.strip().split('\n'))
    }


def execute(instructions):
    instructions = parse_instructions(instructions)
    register = defaultdict(int)
    sounds = defaultdict(int)
    recovered_sound = None
    i = 0

    while i in instructions:
        name, var, sign, val = INSTRUCTION_SET.findall(instructions[i])[0]
        val = get_val(val, sign, register)

        if name == 'set':
            register[var] = val

        elif name == 'add':
            register[var] += val

        elif name == 'mul':
            register[var] *= val

        elif name == 'mod':
            register[var] %= val

        elif name == 'snd':
            sounds[var] = register.get(var, 0)

        elif name == 'rcv':
            if register.get(var) != 0 and var in sounds:
                register[var] = sounds.get(var)
                recovered_sound = register[var]
                break

        elif name == 'jgz':
            if register.get(var, 0) > 0:
                i += val - 1

        i += 1
    return register, sounds, recovered_sound


def solve(data):
    register, sounds, recovered = execute(data)
    return recovered


class Program:

    def __init__(self, instructions, pid, send_mq, receive_mq):
        self.instructions = parse_instructions(instructions)
        self.register = defaultdict(int)
        self.register['p'] = pid
        self.pid = pid
        self.send_mq = send_mq
        self.receive_mq = receive_mq
        self.send_counter = 0
        self.i = 0
        self.state_ready = True

    @property
    def finished(self):
        return not (self.i in self.instructions)

    def is_blocked(self):
        if self.finished:
            self.state_ready = False
            return True

        if self.state_ready is False and not self.receive_mq:
            return True

    def execute_instruction(self):
        if self.is_blocked():
            return

        name, var, sign, val = INSTRUCTION_SET.findall(self.instructions[self.i])[0]
        val = get_val(val, sign, self.register)

        if name == 'set':
            self.register[var] = val

        elif name == 'add':
            self.register[var] += val

        elif name == 'mul':
            self.register[var] *= val

        elif name == 'mod':
            self.register[var] %= val

        elif name == 'snd':
            self.send_mq.append(self.register.get(var, 0))
            self.send_counter += 1
            print('SEND', self.pid, self.send_counter)

        elif name == 'rcv':
            if len(self.receive_mq) > 0:
                #print(self.pid, self.receive_mq)
                self.register[var] = self.receive_mq.popleft()
                self.state_ready = True
            else:
                #print
                self.state_ready = False
                #print(f'LOCKED: {self.pid} {self.send_counter}')
                return

        elif name == 'jgz':
            if self.register.get(var, 0) > 0:
                self.i += val - 1

        self.i += 1


def execute2(data):
    send0_receive1 = deque()
    send1_receive0 = deque()

    program0 = Program(data, 0, send_mq=send0_receive1, receive_mq=send1_receive0)
    program1 = Program(data, 1, send_mq=send1_receive0, receive_mq=send0_receive1)

    while program0.state_ready or program1.state_ready:
        program0.execute_instruction()
        program1.execute_instruction()

    return program0, program1


def solve2(data):
    p0, p1 = execute2(data)
    return p1.send_counter

# your answer is too low. You guessed 129.

if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')