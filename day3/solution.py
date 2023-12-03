import requests
from typing import Tuple, Optional, Dict

def check_if_adjacent_of_symbol(matrix, i, j) -> bool:
    #NW
    if i > 0 and j > 0 and matrix[i - 1][j - 1] != '.':
        return True
    #N
    if i > 0 and matrix[i - 1][j] != '.':
        return True
    #NE
    if i > 0 and j < len(matrix[i]) - 1 and matrix[i - 1][j + 1] != '.':
        return True

    #W
    if j > 0 and matrix[i][j - 1] != '.' and not matrix[i][j - 1].isdigit():
        return True

    #E
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] != '.' and not matrix[i][j + 1].isdigit():
        return True

    #SW
    if i < len(matrix) - 1 and j > 0 and matrix[i + 1][j - 1] != '.':
        return True

    #S
    if i < len(matrix) -1 and matrix[i + 1][j] != '.':
        return True

    #SE
    if i < len(matrix) -1 and j < len(matrix[i]) - 1 and matrix[i + 1][j + 1] != '.':
        return True

    return False

def check_if_adjacent_to_gear(matrix, i, j) -> Optional[Tuple[int, int]]:
    #NW
    if i > 0 and j > 0 and matrix[i - 1][j - 1] == '*':
        return i - 1, j - 1
    #N
    if i > 0 and matrix[i - 1][j] == '*':
        return i - 1, j
    #NE
    if i > 0 and j < len(matrix[i]) - 1 and matrix[i - 1][j + 1] == '*':
        return i - 1, j + 1

    #W
    if j > 0 and matrix[i][j - 1] == '*':
        return i, j - 1

    #E
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] == '*':
        return i, j + 1

    #SW
    if i < len(matrix) - 1 and j > 0 and matrix[i + 1][j - 1] == '*':
        return i + 1, j - 1

    #S
    if i < len(matrix) -1 and matrix[i + 1][j] == '*':
        return i + 1, j

    #SE
    if i < len(matrix) -1 and j < len(matrix[i]) - 1 and matrix[i + 1][j + 1] == '*':
        return i + 1, j + 1

    return None

if __name__ == '__main__':
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    lines = requests.get("https://adventofcode.com/2023/day/3/input", headers=headers).text.splitlines()
    matrix = list(map(list, lines))
    current_number = ''
    adjacent = False
    gear: Optional[Tuple[int, int]] = None
    gears: Dict[Tuple[int, int], int] = {}
    sum1 = 0
    sum2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                current_number += matrix[i][j]

                # Part 1
                if check_if_adjacent_of_symbol(matrix, i, j):
                    adjacent = True

                # Part 2
                match check_if_adjacent_to_gear(matrix, i, j):
                    case gi, gj:
                        gear = gi, gj

            else:
                if len(current_number):

                    # Part 1
                    if adjacent:
                        sum1 += int(current_number)

                    # Part 2
                    match gear:
                        case gi, gj:
                            if (gi, gj) in gears:
                                sum2 += gears.get((gi, gj)) * int(current_number)
                            else:
                                gears.update({(gi, gj): int(current_number)})

                current_number = ''
                adjacent = False
                gear = None
    print("Part 1: ", sum1)
    print("Part 2: ", sum2)


