import requests
from math import sqrt, ceil, floor

def solve(time, distance):
    delta = time ** 2 - 4 * (-1) * (-distance)
    a1 = (-time - sqrt(delta)) / -2
    a2 = (-time + sqrt(delta)) / -2
    lower = min(a1, a2)
    higher = max(a1, a2)
    left = ceil(lower)
    if lower.is_integer():
        left = int(lower) + 1
    right = floor(higher)
    if higher.is_integer():
        right = int(higher) - 1
    return left, right

def main():
    input = read_input()
    # input = open("test_input").readlines()
    times = list(map(lambda x: int(x), input[0].split(":")[1].split()))
    distances = list(map(lambda x: int(x), input[1].split(":")[1].split()))

    product = 1
    for i in range(len(times)):
        left, right = solve(times[i], distances[i])
        product *= right - left + 1

    time = int("".join(input[0].split(":")[1].split()))
    distance = int("".join(input[1].split(":")[1].split()))

    left, right = solve(time, distance)

    return product, right - left + 1

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/6/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
