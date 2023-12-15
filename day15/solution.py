import requests

def hasher(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def solve_part_1(input):
    counter = 0
    for elem in input[0].strip().split(','):
        counter += hasher(elem)
    return counter

def solve_part_2(input):
    boxes = {}
    for elem in input[0].strip().split(','):
        if '=' in elem:
            label, focal_length = elem.split('=')
            box_num = hasher(label)
            box = {}
            if box_num in boxes:
                box = boxes.get(box_num)
            box.update({label: focal_length})
            boxes.update({box_num: box})
        elif '-' in elem:
            label = elem[:-1]
            box_num = hasher(label)
            if box_num in boxes:
                box = boxes.get(box_num)
                if label in box:
                    del box[label]
                boxes.update({box_num: box})
    total_focus_power = 0
    for box_num, box in boxes.items():
        for slot_num, (label, focal_length) in enumerate(box.items(), 1):
            total_focus_power += (box_num + 1) * slot_num * int(focal_length)
    return total_focus_power

def main():
    input = read_input()
    # input = open("test_input").readlines()

    return solve_part_1(input), solve_part_2(input)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/15/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])