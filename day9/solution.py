import requests

def solve_part_1():
    counter = 0
    return counter


def solve_part_2():
    counter = 0
    return counter

def main():
    # input = read_input()
    input = open("test_input").readlines()

    return solve_part_1(), solve_part_2()

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/9/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
