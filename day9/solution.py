import requests

def calculate_lines_below(nums_below):
    lines_below = []
    while len(lines_below) == 0 or not all(map(lambda x: x == 0, lines_below[len(lines_below) - 1])):
        prev_nums_below = nums_below
        nums_below = []
        prev_num = None
        for num in prev_nums_below:
            if prev_num is not None:
                nums_below.append(num - prev_num)
            prev_num = num
        lines_below.append(nums_below)
    return lines_below

def solve_part_1(input_lines):
    sum = 0
    for line in input_lines:
        nums_below = list(map(int, line.split()))
        last_num = nums_below[-1]
        lines_below = calculate_lines_below(nums_below)
        prev_num = 0
        for nums_below in lines_below[::-1]:
            prev_num += nums_below[-1]
        prev_num += last_num
        sum += prev_num
    return sum


def solve_part_2(input_lines):
    sum = 0
    for line in input_lines:
        nums_below = list(map(int, line.split()))
        last_num = nums_below[-1]
        first_num = nums_below[0]
        lines_below = calculate_lines_below(nums_below)
        prev_num = 0
        for nums_below in lines_below[::-1]:
            prev_num = nums_below[0] - prev_num
        prev_num = first_num - prev_num
        sum += prev_num
    return sum

def main():
    input = read_input()
    # input = open("test_input").readlines()
    return solve_part_1(input), solve_part_2(input)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/9/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
