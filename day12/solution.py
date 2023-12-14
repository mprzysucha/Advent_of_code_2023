import requests
from functools import cache

@cache
def replace_and_check(springs, nums, block = 0):

    if springs.count("#") > sum(nums):
        return 0

    if springs.count("?") == 0:
        springs_parts = list(filter(lambda s: len(s.strip()) > 0, springs.split(".")))
        if len(nums) != len(springs_parts):
            return 0
        for i in range(len(springs_parts)):
            if i > 0:
                if len(springs_parts[i]) != nums[i]:
                    return 0
            else:
                if len(springs_parts[i]) + block != nums[i]:
                    return 0
        # print("[" + current + springs + "]")
        return 1

    count = 0

    if springs.startswith('#'):
        if nums[0] - block > 1:
            count += replace_and_check(springs[1:], nums, block + 1) #, current + '#')
        else:
            if springs[1] == '.' or springs[1] == '?':
                count += replace_and_check(springs[2:], nums[1:], 0) #, current + '#.')
            elif springs[1] == '#':
                return 0

    elif springs.startswith("?"):
        if len(nums) > 0 and nums[0] - block > 0:
            count += replace_and_check('#' + springs[1:], nums, block) #, current)
        if block == 0:
            count += replace_and_check('.' + springs[1:], nums, block) #, current)
    elif springs.startswith('.'):
        if block == 0:
            count += replace_and_check(springs[1:], nums, 0) #, current + ".")
        else:
            return 0

    return count

def solve(input):
    part1, part2 = 0, 0
    for line in input:
        [springs, nums_str] = list(map(lambda s: s.strip(), line.split(" ")))
        nums = list(map(int, nums_str.split(",")))
        part1 += replace_and_check(springs, tuple(nums))

        springs = '?'.join([springs] * 5)
        nums_str = ','.join([nums_str] * 5)
        nums = list(map(int, nums_str.split(",")))

        part2 += replace_and_check(springs, tuple(nums))

    return [part1, part2]

def main():
    input = read_input()
    # input = open("test_input").readlines()

    return solve(input)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/12/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
