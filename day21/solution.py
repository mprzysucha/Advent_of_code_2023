import requests
from math import ceil

def calculate_max_steps(matrix, max_steps):
    changes = 1
    while changes > 0:
        changes = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '#':
                    continue
                old_val = max_steps[r][c]
                if r == 0:
                    if c == 0:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r + 1][c] + 1, max_steps[r][c + 1] + 1)
                    elif c == len(max_steps[0]) - 1:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r + 1][c] + 1, max_steps[r][c - 1] + 1)
                    else:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r + 1][c] + 1, max_steps[r][c - 1] + 1, max_steps[r][c + 1] + 1)
                elif r == len(matrix) - 1:
                    if c == 0:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r][c + 1] + 1)
                    elif c == len(max_steps[0]) - 1:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r][c - 1] + 1)
                    else:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r][c - 1] + 1, max_steps[r][c + 1] + 1)
                else:
                    if c == 0:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r + 1][c] + 1, max_steps[r][c + 1] + 1)
                    elif c == len(max_steps[0]) - 1:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r + 1][c] + 1, max_steps[r][c - 1] + 1)
                    else:
                        max_steps[r][c] = min(max_steps[r][c], max_steps[r - 1][c] + 1, max_steps[r + 1][c] + 1, max_steps[r][c - 1] + 1, max_steps[r][c + 1] + 1)
                if max_steps[r][c] != old_val:
                    changes += 1

# def create_matrix_with_start(input, start_defined):
#     width = len(input[0].strip())
#     height = len(input)
#     matrix = []
#     max_steps = []
#     start = [-1, -1]
#     for row_idx, row in enumerate(input):
#         matrix.append([])
#         max_steps.append([])
#         for col_idx, c in enumerate(row.strip()):
#             if c == 'S':
#                 c = '.'
#             matrix[row_idx].append(c)
#             max_steps[row_idx].append(width * height + 1)
#             if row_idx == start_defined[0] and col_idx == start_defined[1]:
#                 start = [row_idx, col_idx]
#                 max_steps[row_idx][col_idx] = 0
#     return matrix, max_steps, start

def create_matrix(input):
    width = len(input[0].strip())
    height = len(input)
    matrix = []
    max_steps = []
    start = [-1, -1]
    for row_idx, row in enumerate(input):
        matrix.append([])
        max_steps.append([])
        for col_idx, c in enumerate(row.strip()):
            matrix[row_idx].append(c)
            max_steps[row_idx].append(width * height + 1)
            if c == 'S':
                start = [row_idx, col_idx]
                max_steps[row_idx][col_idx] = 0
    return matrix, max_steps, start

def find_solution_part1(matrix, max_steps, num_of_steps):
    counter = 0
    b = min(num_of_steps, len(max_steps) * len(max_steps[0]) - 1)
    steps_needed = 0
    for r in range(len(max_steps)):
        for c in range(len(max_steps[0])):
            if num_of_steps % 2 == max_steps[r][c] % 2 and max_steps[r][c] <= b and matrix[r][c] != '#':
                if max_steps[r][c] > steps_needed:
                    steps_needed = max_steps[r][c]
                counter += 1
    return counter, steps_needed

def solve_part_1(input, num_of_steps):
    matrix, max_steps, start = create_matrix(input)
    calculate_max_steps(matrix, max_steps)
    part1, _ = find_solution_part1(matrix, max_steps, num_of_steps)
    return part1

def change_start(input, change):
    h, w = len(input), len(input[0])
    m = int((h - 1) / 2)
    input[0] = "".join([change[0][0], input[0][1:m], change[0][1], input[0][m+1:-1], change[0][2]])
    input[m] = "".join([change[1][0], input[m][1:m], change[1][1], input[m][m+1:-1], change[1][2]])
    input[h - 1] = "".join([change[2][0], input[h - 1][1:m], change[2][1], input[h - 1][m+1:-1], change[2][2]])
    return input

def solve_part_2(input, num_of_steps):

    input = list(map(lambda row: row.strip(), input))

    matrix, max_steps, start = create_matrix(input)
    calculate_max_steps(matrix, max_steps)
    all_achievable_in_square_from_middle_point, steps_needed_form_middle_point = find_solution_part1(matrix, max_steps, num_of_steps)

    h, w = len(input), len(input[0])
    m = int((h - 1) / 2)
    n = ceil((num_of_steps - m) / h) # (26501365 - 65) / 131 = 202300

    matrix_up_right, max_steps_up_right, _ = create_matrix(change_start(input, [['.', '.', '.'], ['.', '.', '.'], ['S', '.', '.']]))
    calculate_max_steps(matrix_up_right, max_steps_up_right)
    # all_achievable_up_right, steps_needed_up_right = find_solution_part1(matrix_up_right, max_steps_up_right, num_of_steps)

    matrix_up_left, max_steps_up_left, _ = create_matrix(change_start(input, [['.', '.', '.'], ['.', '.', '.'], ['.', '.', 'S']]))
    calculate_max_steps(matrix_up_left, max_steps_up_left)
    # all_achievable_up_left, steps_needed_up_left = find_solution_part1(matrix_up_left, max_steps_up_left, num_of_steps)

    matrix_down_right, max_steps_down_right, _ = create_matrix(change_start(input, [['S', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]))
    calculate_max_steps(matrix_down_right, max_steps_down_right)
    # all_achievable_down_right, steps_needed_down_right = find_solution_part1(matrix_down_right, max_steps_down_right, num_of_steps)

    matrix_down_left, max_steps_down_left, _ = create_matrix(change_start(input, [['.', '.', 'S'], ['.', '.', '.'], ['.', '.', '.']]))
    calculate_max_steps(matrix_down_left, max_steps_down_left)
    # all_achievable_down_left, steps_needed_down_left = find_solution_part1(matrix_down_left, max_steps_down_left, num_of_steps)

    matrix_left, max_steps_left, _ = create_matrix(change_start(input, [['.', '.', '.'], ['.', '.', 'S'], ['.', '.', '.']]))
    calculate_max_steps(matrix_left, max_steps_left)
    # all_achievable_left, steps_needed_left = find_solution_part1(matrix_left, max_steps_left, num_of_steps)

    matrix_right, max_steps_right, _ = create_matrix(change_start(input, [['.', '.', '.'], ['S', '.', '.'], ['.', '.', '.']]))
    calculate_max_steps(matrix_right, max_steps_right)
    # all_achievable_right, steps_needed_right = find_solution_part1(matrix_right, max_steps_right, num_of_steps)

    matrix_up, max_steps_up, _ = create_matrix(change_start(input, [['.', '.', '.'], ['.', '.', '.'], ['.', 'S', '.']]))
    calculate_max_steps(matrix_up, max_steps_up)
    # all_achievable_up, steps_needed_up = find_solution_part1(matrix_up, max_steps_up, num_of_steps)

    matrix_down, max_steps_down, _ = create_matrix(change_start(input, [['.', 'S', '.'], ['.', '.', '.'], ['.', '.', '.']]))
    calculate_max_steps(matrix_down, max_steps_down)
    # all_achievable_down, steps_needed_down = find_solution_part1(matrix_down, max_steps_down, num_of_steps)

    # 26501365 - 65 / 131

    # 7574 + 7612 +

    # go right, left, up, down

    # first on the right/left/up/down: 26501365 - 65 - 1 = 26501299
    #     7574,     7612,     7574,     7612, 7574, 7612, ...
    # 26501299, 26501168, 26501037, 26500906, ...

    #
    # 101149 tuples (7574 + 7612)
    # the last tuple:
    # up: 261 steps remaining: 7574 + 130 steps remaining: 5682
    # down: 261 steps remaining: 7574 + 130 steps remaining: 5688
    # left: 261 steps remaining: 7574 + 130 steps remaining: 5694
    # right: 261 steps remaining: 7574 + 130 steps remaining: 5676

    __up = find_solution_part1(matrix_up, max_steps_up, 130)[0]
    # up: 5705

    __down = find_solution_part1(matrix_down, max_steps_down, 130)[0]
    # down: 5717

    __left = find_solution_part1(matrix_left, max_steps_left, 130)[0]
    # left: 5700

    __right = find_solution_part1(matrix_right, max_steps_right, 130)[0]
    # right: 5722


    achievable_in_lines = 4 * 101149 * (7574 + 7612) + 4 * 7612 + 5705 + 5717 + 5700 + 5722 # 6144248148

    # corner up-right:
    #     7574,   2*7612,   3*7574,   4x7612, ...
    # 26501233, 26501102, 26500971, 26500840, ....

    # 101149*262 = 26501038
    # 101150*262-67 = 26501233
    # 101149*262+195 = 26501233

    # 64:
    # up right:  954
    # up left: 970
    # down right: 964
    # down left: 966

    # 195:
    # up right: 6645
    # up left: 6634
    # down right: 6651
    # down left: 6640

    # 1, 3, 5, 7, a1 = 1, a2 = a1 + 2, a3 = a1 + 2*2, an = a1 + 2*(n-1), a(101149) = 1 + 2*(101149-1) = 202297
    # a(101150) = 1 + 2*(101150-1) = 202299
    # sum: (a1 + a(101149))/2*101149 = (1 + 202297)/2*101149 = 10231120201
    # sum: (a1 + a(101150))/2*101150 = (1 + 202299)/2*101150 = 10231322500
    # 2, 4, 6, 8
    # sum: 10231221350

    all_achievable_in_diagonals = 4 * 10231120201 * 7574 + 4 * 10231221350 * 7612 + 202299 * (6645 + 6634 + 6651 + 6640) + 202300 * (954 + 970 + 964 + 966)
    # 621488400022926



    # Solution
    # print(7574 + achievable_in_lines + all_achievable_in_diagonals)



    # counter = all_achievable_in_square_from_middle_point
    counter = 7574

    last_diagonal = [0, 0]
    last_line = [0,0]

    counter_lines = 0
    counter_diagonals = 0

    for i in range(1, n + 1):
        d = num_of_steps - m - 1 - h * (i - 1)
        if d > 17161: #if d > w * h:
            if d % 2 == 0:
                counter_lines += 4 * 7574
            else:
                counter_lines += 4 * 7612
            # counter += all_achievable_up + all_achievable_down + all_achievable_left + all_achievable_right
        elif d > 0:
            counter_lines += find_solution_part1(matrix_right, max_steps_right, d)[0]
            counter_lines += find_solution_part1(matrix_left, max_steps_left, d)[0]
            counter_lines += find_solution_part1(matrix_up, max_steps_up, d)[0]
            counter_lines += find_solution_part1(matrix_down, max_steps_down, d)[0]
            last_line = [i, d]
        d = num_of_steps - 1 - h * i
        if d > 17161: #w * h:
            if d % 2 == 0:
                counter_diagonals += i * 4 * 7612
            else:
                counter_diagonals += i * 4 * 7574
            # counter += i * (all_achievable_up_right + all_achievable_up_left + all_achievable_down_right + all_achievable_down_left)
        elif d > 0:
            counter_diagonals += i * find_solution_part1(matrix_up_right, max_steps_up_right, d)[0]
            counter_diagonals += i * find_solution_part1(matrix_up_left, max_steps_up_left, d)[0]
            counter_diagonals += i * find_solution_part1(matrix_down_right, max_steps_down_right, d)[0]
            counter_diagonals += i * find_solution_part1(matrix_down_left, max_steps_down_left, d)[0]
            last_diagonal = [i, d]

    print("last_line:", last_line)
    print("last_diagonal:", last_diagonal)

    print("counter:", counter, "all_achievable_in_square_from_middle_point:", all_achievable_in_square_from_middle_point)
    print("counter_lines:", counter_lines, "achievable_in_lines:", achievable_in_lines)
    print("counter_diagonals:", counter_diagonals, "all_achievable_in_diagonals:", all_achievable_in_diagonals)
    print("counters sum:", counter + counter_lines + counter_diagonals)
    print("all_achievables sum:", all_achievable_in_square_from_middle_point + achievable_in_lines + all_achievable_in_diagonals)

    return counter + counter_lines + counter_diagonals

def main():
    input = read_input()
    # input = open("test_input").readlines()

    # return solve_part_1(input, 64), solve_part_2(input, 10)
    return solve_part_1(input, 64), solve_part_2(input, 26501365)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/21/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])