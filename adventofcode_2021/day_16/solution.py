"""Day 16: Packet Decoder

https://adventofcode.com/2021/day/16



BITE           ---> 0 | 1
VERSION        ---> BITE BITE BITE
TYPE-ID        ---> BITE BITE BITE
LENGTH-ID      ---> BITE

GROUP          ---> 1 BITE BITE BITE BITE
END            ---> 0 BITE BITE BITE BITE
VALUE          ---> GROUP GROUP | END | VALUE

PACKET         ---> VERSION TYPE-ID VALUE |
                    VERSION TYPE-ID LENGTH-ID-0 BITE-15 PACKET |
                    VERSION TYPE-ID LENGTH-ID-1 BITE-11 PACKET |
                    PACKET PACKET |
                    ''

"""
import operator
from abc import ABC, abstractmethod
from functools import reduce

HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

BIN_TO_HEX = {
    v: k for k, v in HEX_TO_BIN.items()
}

INSTRUCTIONS = {
    '0': sum,
    '1': lambda x: reduce(operator.mul, x, 1),
    '2': min,
    '3': max,
    '5': lambda x: int(x[0] > x[1]),
    '6': lambda x: int(x[0] < x[1]),
    '7': lambda x: int(x[0] == x[1])
}


def hexadecimal_to_binary(hexadecimal):
    """
    Args: hexadecimal
    Returns: PACKET
    """
    return ''.join([
        HEX_TO_BIN[h] for h in hexadecimal
    ])


def split_packet(packet, pos):
    return packet[:pos], packet[pos:]


def parse_packet(packet, version_sum=0):
    """
    Args: packet, version_sum
    Returns: version_sum
    """
    if packet == '' or all([i == '0' for i in packet]):
        return version_sum

    version, packet = split_packet(packet, 3)
    type_id, packet = split_packet(packet, 3)
    version_sum += int(f'0{version}', 2)

    if type_id == '100':
        end = False
        while not end:
            group, packet = split_packet(packet, 5)
            if group[0] == '0':
                end = True

        return parse_packet(packet, version_sum)

    else:
        length_id, packet = split_packet(packet, 1)
        if length_id == '0':
            num, packet = split_packet(packet, 15)

        elif length_id == '1':
            num, packet = split_packet(packet, 11)
        return parse_packet(packet, version_sum)


def solve(data):
    packet = hexadecimal_to_binary(data.strip())
    return parse_packet(packet)


class Parser:

    @staticmethod
    def split_seq(seq, pos):
        return seq[:pos], seq[pos:]

    @staticmethod
    def normalize_seq(seq):
        return seq if any([i == '1' for i in seq]) else ''

    @staticmethod
    def get_id_3(seq):
        id, seq = Parser.split_seq(seq, 3)
        id_value = BIN_TO_HEX[f'0{id}']
        return id_value, seq

    @staticmethod
    def get_length_value(seq, length_id):
        if length_id == '0':
            length, seq = Parser.split_seq(seq, 15)
        elif length_id == '1':
            length, seq = Parser.split_seq(seq, 11)
        return int(length, 2), seq

    @staticmethod
    def get_package(seq):
        version, seq = Parser.get_id_3(seq)
        type_id, seq = Parser.get_id_3(seq)
        instr = INSTRUCTIONS.get(type_id, None)
        if not instr:
            return LiteralPackage(version, type_id, seq)
        length_id, seq = Parser.split_seq(seq, 1)
        length, seq = Parser.get_length_value(seq, length_id)
        return OperatorPackage(version, type_id, seq, length_id, length, instr)


class Package(ABC):

    def __init__(self, version, type_id, seq):
        self.version = version
        self.type_id = type_id
        self.seq = seq

    def __repr__(self):
        return self.seq

    @abstractmethod
    def get_value(self):
        """Return: value, seq"""
        pass


class LiteralPackage(Package):

    def get_value(self):
        to_encode = ''
        end = False
        while not end:
            group, self.seq = Parser.split_seq(self.seq, 5)
            to_encode += group[1:]
            if group[0] == '0':
                end = True
        return int(to_encode, 2), self.seq


class OperatorPackage(Package):

    def __init__(self, version, type_id, seq, length_id, length, instruction):
        super().__init__(version, type_id, seq)
        self.length_id = length_id
        self.length = length
        self.instruction = instruction
        self.children = []
        self.is_ready = False

    def get_value(self):
        while not self.is_ready:
            self.evaluate()
        return (
            self.instruction(self.children),
            Parser.normalize_seq(self.seq)
        )

    def evaluate_0(self):
        new_seq, self.seq = Parser.split_seq(self.seq, self.length)
        while new_seq:
            new_package = Parser.get_package(new_seq)
            value, new_seq = new_package.get_value()
            self.children.append(value)
        self.is_ready = True

    def evaluate_1(self):
        while self.length and self.seq:
            new_package = Parser.get_package(self.seq)
            value, self.seq = new_package.get_value()
            self.children.append(value)
            self.length -= 1
        self.is_ready = True

    def evaluate(self):
        if self.length_id == '0':
            # total length
            return self.evaluate_0()
        elif self.length_id == '1':
            # number of subpackages
            return self.evaluate_1()


def solve2(data):
    seq = hexadecimal_to_binary(data.strip())
    package = Parser.get_package(seq)
    return package.get_value()[0]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
