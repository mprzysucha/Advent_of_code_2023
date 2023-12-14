import requests
import time
from functools import cache
from copy import deepcopy

def prettyprint(input):
    print('-' * len(input[0]))
    for line in input:
        print(line.strip())
    print('-' * len(input[0]))

def prettyprintuple(input):
    print('-' * len(input[0]))
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end = '')
        print()
    print('-' * len(input[0]))

@cache
def move_N(tuple0):
    input = to_list(tuple0)
    # input = deepcopy(input0)
    change = True
    while change:
        change = False
        for i in range(1, len(input)):
            for j in range(len(input[i])):
                prev_c = input[i-1][j]
                current_c = input[i][j]
                if current_c == 'O' and prev_c == '.':
                    input[i] = input[i][:j] + '.' + input[i][j+1:]
                    input[i - 1] = input[i - 1][:j] + 'O' + input[i - 1][j+1:]
                    change = True
    return to_tuple(input)

@cache
def move_S(tuple0):
    input = to_list(tuple0)
    # input = deepcopy(input0)
    change = True
    while change:
        change = False
        for i in range(len(input) - 2, -1, -1):
            for j in range(len(input[i])):
                prev_c = input[i+1][j]
                current_c = input[i][j]
                if current_c == 'O' and prev_c == '.':
                    input[i] = input[i][:j] + '.' + input[i][j+1:]
                    input[i + 1] = input[i + 1][:j] + 'O' + input[i + 1][j+1:]
                    change = True
    return to_tuple(input)

@cache
def move_E(tuple0):
    input = to_list(tuple0)
    # input = deepcopy(input0)
    change = True
    while change:
        change = False
        for j in range(len(input[0]) - 2, -1, -1):
            for i in range(len(input)):
                prev_c = input[i][j + 1]
                current_c = input[i][j]
                if current_c == 'O' and prev_c == '.':
                    input[i] = input[i][:j] + '.O' + input[i][j + 2:]
                    change = True
    return to_tuple(input)

@cache
def move_W(tuple0):
    input = to_list(tuple0)
    # input = deepcopy(input0)
    change = True
    while change:
        change = False
        for j in range(1, len(input[0])):
            for i in range(len(input)):
                prev_c = input[i][j - 1]
                current_c = input[i][j]
                if current_c == 'O' and prev_c == '.':
                    input[i] = input[i][:j - 1] + 'O.' + input[i][j + 1:]
                    change = True
    return to_tuple(input)

def load(input0):
    counter = 0
    for i in range(len(input0)):
        weight = len(input0) - i
        for j in range(len(input0[i])):
            if input0[i][j] == 'O':
                counter += weight
    return counter

# @cache

prev_hash = 0
hashes = set()
found_cycle = False
next_hash = {}
cycle_start = -1
cycle_end = -1
memory = {}

def cycle(input0, i):
    global found_cycle, prev_hash, hashes, next_hash, cycle_start, cycle_end, memory
    h = hash(input0)
    if h in hashes:
        if found_cycle:
            if prev_hash in next_hash:
                cycle_end = i
            else:
                next_hash.update({prev_hash: h})
        else:
            cycle_start = i
            found_cycle = True
        prev_hash = h
    else:
        hashes.add(h)
    table_after_cycle = move_E(move_S(move_W(move_N(input0))))
    if not i in memory:
        memory.update({i:table_after_cycle})
    return table_after_cycle

@cache
def cycle_1(input0):
    return move_E(move_S(move_W(move_N(input0))))

@cache
def cycles_1000(input0):
    for _ in range(1000):
        input0 = cycle_1(input0)
    return input0

def to_tuple(input):
    t = ()
    for i in range(len(input)):
        ti = ()
        for j in range(len(input[i])):
            ti = ti + (input[i][j],)
        t = t + (ti,)
    return t

def to_list(input):
    l = []
    for i in range(len(input)):
        li = []
        for j in range(len(input[i])):
            li.append(input[i][j])
        l.append("".join(li))
    return l

def solve_part_1(input0):
    start = time.thread_time_ns()
    input1 = to_list(move_N(to_tuple(input0)))
    counter = load(input1)
    end = time.thread_time_ns()
    print("Part 1 time:", str((end - start) / 1_000_000))
    return counter

def solve_part_2(input):
    global cycle_start, cycle_end, memory
    start = time.thread_time_ns()
    input = to_tuple(input)
    for i in range(1_000_000):
        input = cycles_1000(input)
    # for i in range(1_000_000_000):
    #     if cycle_start != -1 and cycle_end != -1:
    #         cycle_len = cycle_end - cycle_start
    #         no_iters_in_cycles = 1_000_000_001 - cycle_start
    #         no_iters_remaining = no_iters_in_cycles % cycle_len
    #         cycle_number_to_check = cycle_start + no_iters_remaining - 1
    #         end = time.thread_time_ns()
    #         print("Part 2 time:", str((end - start) / 1_000_000))
    #         return load(memory.get(cycle_number_to_check))
    #     input = cycle(input, i + 1)

    print("Part 2 after 1_000_000_000 cycles:")
    prettyprintuple(input)
    counter = load(input)
    end = time.thread_time_ns()
    print("Part 2 time:", str((end - start) / 1_000_000))
    return counter

def main():
    input = read_input()
    # input = open("test_input").readlines()

    input = list(map(lambda s: s.strip(), input))

    return solve_part_1(input), solve_part_2(input)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/14/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])