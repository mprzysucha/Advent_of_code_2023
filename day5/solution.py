import requests

def main():
    input = read_input()
    # input = open("test_input").readlines()
    key = ""
    nums = []
    ranges_part_2 = []
    changed = []
    ranges_part_2_changed = []
    for line in input:
        if line.startswith("seeds"):
            nums = list(map(int, line.split("seeds: ")[1].split(" ")))
            for i in range(0, len(nums) - 1, 2):
                ranges_part_2.append([nums[i], nums[i] + nums[i + 1]])
        elif line.strip().endswith("map:"):
            key = line.strip().split("map:")[0]

            # Part 1
            changed = []

            # Part 2
            ranges_part_2_changed = []

        elif len(line.strip()) == 0 and len(key.strip()) > 0:
            # Part 2 only
            ranges_part_2.extend(ranges_part_2_changed)
        elif len(line.strip()) > 0:
            [dst_start, src_start, length] = list(map(int, line.split(" ")))

            # Part 1
            for i, num in enumerate(nums):
                if num in range(src_start, src_start + length) and not i in changed:
                    nums[i] = num + dst_start - src_start
                    changed.append(i)

            # Part 2
            ranges_part_2_not_changed = []
            for i, range_in in enumerate(ranges_part_2):
                match intersection(range_in, [src_start, src_start + length]):
                    case None:
                        ranges_part_2_not_changed.append([range_in[0], range_in[1]])
                    case l, r:
                        if l > range_in[0]:
                            ranges_part_2_not_changed.append([range_in[0], l])
                        ranges_part_2_changed.append([l + (dst_start - src_start), r + (dst_start - src_start)])
                        if r < range_in[1]:
                            ranges_part_2_not_changed.append([r, range_in[1]])
            ranges_part_2 = ranges_part_2_not_changed
    # Part 2 needed
    ranges_part_2.extend(ranges_part_2_changed)

    return min(nums), min(list(map(lambda x: x[0], ranges_part_2)))


def intersection(r1: [int, int], r2: [int, int]):
    left = max(r1[0], r2[0])
    right = min(r1[1], r2[1])
    if left < right:
        return [left, right]
    else:
        return None

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/5/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
