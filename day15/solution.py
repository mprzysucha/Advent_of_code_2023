import requests

def solve_part_1(input):
    counter = 0
    return counter


def solve_part_2(input):
    counter = 0
    return counter

def main():
    # input = read_input()
    input = open("test_input").readlines()

    return solve_part_1(input), solve_part_2(input)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/14/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])