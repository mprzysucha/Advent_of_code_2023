import requests
import time

def solve_part_1(input):
    return solve(input, expand_size = 2)

def solve_part_2(input):
    return solve(input, expand_size = 1000000)

def solve(input, expand_size):
    input_expanded = []
    for row in input:
        input_expanded.append(row.strip())
        if all(map(lambda c: c == '.', row.strip())):
            input_expanded.append("*" * len(row.strip()))
    columns_to_expand = []
    for col_num in range(0, len(input[0])):
        all_dots_in_this_column = True
        for row_num in range(0, len(input)):
            if input[row_num][col_num] != '.':
                all_dots_in_this_column = False
                break
        if all_dots_in_this_column:
            columns_to_expand.append(col_num + len(columns_to_expand))
    for col_to_expand in columns_to_expand:
        for row_num in range(0, len(input_expanded)):
            input_expanded[row_num] = input_expanded[row_num][:col_to_expand + 1] + '*' + input_expanded[row_num][col_to_expand + 1:]

    galaxies_coords = []
    for row_num in range(0, len(input_expanded)):
        for col_num in range(0, len(input_expanded[row_num])):
            if input_expanded[row_num][col_num] == '#':
                galaxies_coords.append([row_num, col_num])

    counter = 0
    for galaxy1_idx in range(0, len(galaxies_coords)):
        for galaxy2_idx in range(galaxy1_idx + 1, len(galaxies_coords)):
            g1_row, g1_col = galaxies_coords[galaxy1_idx]
            g2_row, g2_col = galaxies_coords[galaxy2_idx]
            left, right = min(g1_col, g2_col), max(g1_col, g2_col)
            horizontal_path = input_expanded[g1_row][left:right+1]
            horizontal_steps = horizontal_path.count('.') + (expand_size - 1) * horizontal_path.count('*') + horizontal_path.count("#") - 1

            vertical_path = []
            top, bottom = min(g1_row, g2_row), max(g1_row, g2_row)
            for vp_row in range(top, bottom + 1):
                vertical_path.append(input_expanded[vp_row][g1_col])
            vertical_steps = vertical_path.count('.') + (expand_size - 1) * vertical_path.count("*") + vertical_path.count("#") - 1

            counter += (horizontal_steps + vertical_steps)

    return counter

def main():
    input = read_input()
    # input = open("test_input").readlines()
    start = time.time()
    part1 = solve_part_1(input)
    part2 = solve_part_2(input)
    end = time.time()
    return part1, part2, 1000 * (end - start)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/11/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
    print("Time: ", result[2])
