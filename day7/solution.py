import requests
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key

class HandType(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

@dataclass
class Hand:
    def __init__(self, hand: str):
        self.hand = hand.upper()
        self.__cards = {}
        self.__cards_without_joker = {}
        self.type = HandType.HIGH_CARD
        self.type_with_joker = HandType.HIGH_CARD
        self.__calculate_cards_counter()
        self.__calculate_cards_counter_without_jokers()
        self.__calculate_type()
        self.__calculate_type_with_jokers()

    # Part 1
    def __calculate_cards_counter(self):
        self.__cards = dict(map(lambda c: (c, self.hand.count(c)), set(self.hand)))

    # Part 2
    def __calculate_cards_counter_without_jokers(self):
        self.__cards_without_joker = dict(map(lambda c: (c, self.hand.count(c)), set(filter(lambda c: c != 'J', set(self.hand)))))

    def __calculate_type(self):
        card_vals = list(self.__cards.values())
        if card_vals.count(5) == 1:
            self.type = HandType.FIVE_OF_A_KIND
        elif card_vals.count(4) == 1:
            self.type = HandType.FOUR_OF_A_KIND
        elif card_vals.count(3) == 1 and card_vals.count(2) == 1:
            self.type = HandType.FULL_HOUSE
        elif card_vals.count(3) == 1 and card_vals.count(2) == 0:
            self.type = HandType.THREE_OF_A_KIND
        elif card_vals.count(2) == 2 and card_vals.count(1) == 1:
            self.type = HandType.TWO_PAIR
        elif card_vals.count(2) == 1 and card_vals.count(1) == 3:
            self.type = HandType.ONE_PAIR
        elif card_vals.count(1) == 5:
            self.type = HandType.HIGH_CARD

    def __calculate_type_with_jokers(self):
        card_vals = list(self.__cards_without_joker.values())
        if card_vals.count(5) == 1:
            self.type_with_joker = HandType.FIVE_OF_A_KIND
        elif card_vals.count(4) == 1:
            if self.__jokers() == 1:
                self.type_with_joker = HandType.FIVE_OF_A_KIND
            else:
                self.type_with_joker = HandType.FOUR_OF_A_KIND
        elif card_vals.count(3) == 1 and card_vals.count(2) == 1:
            self.type_with_joker = HandType.FULL_HOUSE
        elif card_vals.count(3) == 1:
            if self.__jokers() == 2:
                self.type_with_joker = HandType.FIVE_OF_A_KIND
            elif self.__jokers() == 1:
                self.type_with_joker = HandType.FOUR_OF_A_KIND
            else:
                self.type_with_joker = HandType.THREE_OF_A_KIND
        elif card_vals.count(2) == 2:
            if self.__jokers() == 1:
                self.type_with_joker = HandType.FULL_HOUSE
            else:
                self.type_with_joker = HandType.TWO_PAIR
        elif card_vals.count(2) == 1:
            if self.__jokers() == 3:
                self.type_with_joker = HandType.FIVE_OF_A_KIND
            elif self.__jokers() == 2:
                self.type_with_joker = HandType.FOUR_OF_A_KIND
            elif self.__jokers() == 1:
                self.type_with_joker = HandType.THREE_OF_A_KIND
            else:
                self.type_with_joker = HandType.ONE_PAIR
        elif card_vals.count(1) == 5:
            self.type_with_joker = HandType.HIGH_CARD
        elif self.__jokers() == 5:
            self.type_with_joker = HandType.FIVE_OF_A_KIND
        elif self.__jokers() == 4 and card_vals.count(1) == 1:
            self.type_with_joker = HandType.FIVE_OF_A_KIND
        elif self.__jokers() == 3 and card_vals.count(1) == 2:
            self.type_with_joker = HandType.FOUR_OF_A_KIND
        elif self.__jokers() == 2 and card_vals.count(1) == 3:
            self.type_with_joker = HandType.THREE_OF_A_KIND
        elif self.__jokers() == 1 and card_vals.count(1) == 4:
            self.type_with_joker = HandType.ONE_PAIR
        elif self.__jokers() == 0 and card_vals.count(1) == 5:
            self.type_with_joker = HandType.HIGH_CARD

    def __jokers(self):
        return self.hand.count('J')

    def __str__(self):
        return "".join(["Hand(", self.hand, ")"])

    def __repr__(self):
        return str(self)


cards_part_1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
strong_part_1 = list(range(len(cards_part_1), 0, -1))
cards_to_strong_part_1 = dict(zip(cards_part_1, strong_part_1))

cards_part_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
strong_part_2 = list(range(len(cards_part_2), 0, -1))
cards_to_strong_part_2 = dict(zip(cards_part_2, strong_part_2))


def compare_cards(card1: str, card2: str):
    if card1.upper() in [*cards_to_strong_part_1.keys()] and card2.upper() in [*cards_to_strong_part_1.keys()]:
        if cards_to_strong_part_1[card1.upper()] > cards_to_strong_part_1[card2.upper()]:
            return 1
        elif cards_to_strong_part_1[card1.upper()] < cards_to_strong_part_1[card2.upper()]:
            return -1
    return 0


def compare_cards_joker(card1: str, card2: str):
    if card1.upper() in [*cards_to_strong_part_2.keys()] and card2.upper() in [*cards_to_strong_part_2.keys()]:
        if cards_to_strong_part_2[card1.upper()] > cards_to_strong_part_2[card2.upper()]:
            return 1
        elif cards_to_strong_part_2[card1.upper()] < cards_to_strong_part_2[card2.upper()]:
            return -1
    return 0


def compare(hand1: Hand, hand2: Hand):
    if hand1.hand.upper() == hand2.hand.upper():
        return 0
    elif hand1.type.value > hand2.type.value:
        return -1
    elif hand1.type.value < hand2.type.value:
        return 1
    else:
        h1 = hand1.hand.upper()
        h2 = hand2.hand.upper()
        for i in range(len(h1)):
            cmp = compare_cards(h1[i], h2[i])
            if cmp != 0:
                return cmp
        return 0


def compare_joker(hand1: Hand, hand2: Hand):
    if hand1.hand.upper() == hand2.hand.upper():
        return 0
    elif hand1.type_with_joker.value > hand2.type_with_joker.value:
        return -1
    elif hand1.type_with_joker.value < hand2.type_with_joker.value:
        return 1
    else:
        h1 = hand1.hand.upper()
        h2 = hand2.hand.upper()
        for i in range(len(h1)):
            cmp = compare_cards_joker(h1[i], h2[i])
            if cmp != 0:
                return cmp
        return 0

def main():
    input = read_input()
    # input = open("test_input").readlines()

    hands_to_bid = {}
    hands = []
    for line in input:
        split = line.split()
        hands_to_bid[split[0]] = int(split[1])
        hands.append(Hand(split[0]))
    hands_sorted_part_1 = sorted(hands, key=cmp_to_key(compare))
    hands_sorted_part_2 = sorted(hands, key=cmp_to_key(compare_joker))

    sum_part_1 = 0
    sum_part_2 = 0
    for rank in range(1, len(hands_sorted_part_1) + 1):
        sum_part_1 += hands_to_bid[hands_sorted_part_1[rank - 1].hand] * rank
        sum_part_2 += hands_to_bid[hands_sorted_part_2[rank - 1].hand] * rank

    return sum_part_1, sum_part_2

def read_input():
    headers = {'Cookie': 'session={}'.format(open("../sessionId").readline())}
    return requests.get("https://adventofcode.com/2023/day/7/input", headers=headers).text.splitlines()

if __name__ == '__main__':
    result = main()
    print("Part 1: ", result[0])
    print("Part 2: ", result[1]) # 248801421 too low
