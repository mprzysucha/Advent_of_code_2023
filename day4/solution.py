import requests

def main():
    input = read_input()
    # input = open("test_input").readlines()
    sum_of_points = 0 # for Part 1
    num_of_cards = [1 for i in range(len(input))] # for Part 2
    for line in input:
        [[_, card_num_tag, *winners], owned] = list(map(lambda part: part.split(), line.split('|')))
        num_of_matching = len(set(winners).intersection(set(owned)))

        # Part 1
        sum_of_points += int(pow(2, num_of_matching - 1))

        # Part 2
        card_num = int(card_num_tag[:-1]) - 1
        for c in list(range(card_num + 1, card_num + 1 + num_of_matching)):
            num_of_cards[c] += num_of_cards[card_num]

    return sum_of_points, sum(num_of_cards)

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/4/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1])
