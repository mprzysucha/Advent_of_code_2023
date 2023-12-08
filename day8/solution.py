import math

import requests

def solve_part_1(steps, instructions_set):
    counter = 0
    # current_step = input[2][0:3] <- hehe
    current_step = 'AAA'
    instruction_idx = 0
    while current_step != 'ZZZ':
        current_step = steps[current_step][instructions_set[instruction_idx]]
        instruction_idx += 1
        if instruction_idx == len(instructions_set):
            instruction_idx = 0
        counter += 1
    return counter


def solve_part_2(steps, instructions_set):
    current_steps = list(filter(lambda k: k.endswith('A'), steps.keys()))
    counters = []
    for current_step in current_steps:
        instruction_idx = 0
        counter = 0
        while not current_step.endswith('Z'):
            current_step = steps[current_step][instructions_set[instruction_idx]]
            instruction_idx += 1
            if instruction_idx == len(instructions_set):
                instruction_idx = 0
            counter += 1
        counters.append(counter)
    return math.lcm(*counters)

def main():
    input = read_input()
    # input = open("test_input_1").readlines()
    # input = open("test_input_2").readlines()
    # input = open("test_input_3").readlines()

    instructions_set = input[0].strip()
    steps = {}

    for line in input[2:]:
        [src, targets] = line.split(" = ")
        steps.update({src: {'L': targets[1:4], 'R': targets[6:9]}})

    return solve_part_1(steps, instructions_set), solve_part_2(steps, instructions_set)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/8/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1]) # 248801421 too low
