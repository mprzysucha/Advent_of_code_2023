import requests
from operator import mul
from functools import reduce

def main():
    input = read_input()
    # input = open("test_input").readlines()

    sum_part_1 = 0
    sum_part_2 = 0
    for line in input:
        [game_id, reveals] = line.split(":")
        reveal = list(map(lambda s: s.split(', '), list(map(lambda s: s.strip(), reveals.split(";")))))
        if all(map(set_possible, reveal)):
            sum_part_1 += int(game_id.split()[1])
        sum_part_2 += reduce(mul, reduce(min_set, reveal, {'blue': 0, 'red': 0, 'green': 0}).values())
    return sum_part_1, sum_part_2

def set_possible(set):
    for cubes in set:
        [num, color] = cubes.split(" ")
        if (color == 'red' and int(num) > 12) or (color == 'green' and int(num) > 13) or (color == 'blue' and int(num) > 14):
            return False
    return True


def min_set(acc, set):
    for cubes in set:
        [num, color] = cubes.split(" ")
        acc[color] = max(acc[color], int(num))
    return acc


def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/2/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1]) # 248801421 too low
