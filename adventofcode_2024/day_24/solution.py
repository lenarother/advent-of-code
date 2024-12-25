"""Day 24: Crossed Wires

https://adventofcode.com/2024/day/24

"""

def parse_inputs(data):
    inputs_dict = dict()
    for line in data.strip().split('\n\n')[0].splitlines():
        wire, value = line.split(': ')
        inputs_dict[wire] = int(value)
    return inputs_dict

def parse_gates(data):
    gate_dict = dict()
    for line in data.strip().split('\n\n')[1].splitlines():
        w1, gate, w2, _, w3 = line.split(' ')
        gate_dict[(w1, w2, gate, w3)] = w3
    return gate_dict

def calculate(w1, w2, gate):
    if gate == 'AND':
        return w1 & w2
    elif gate == 'OR':
        return w1 | w2
    else:
        return w1 ^ w2


def solve(data):
    inputs = parse_inputs(data)
    gates = parse_gates(data)
    outputs = dict()
    print(inputs)
    print(gates)

    while gates:
        to_remove = []
        for gate, output_wire in gates.items():
            if gate[0] in inputs and gate[1] in inputs:
                output  = calculate(inputs[gate[0]], inputs[gate[1]], gate[2])
                inputs[output_wire] = output
                if output_wire.startswith('z'):
                    outputs[output_wire] = output
                to_remove.append(gate)
        for gate in to_remove:
            gates.pop(gate)
    print(outputs)

    result = ''
    for i in sorted(outputs.keys(), reverse=True):
        result+= str(outputs[i])
    print(result)
    return int(result, 2)



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
