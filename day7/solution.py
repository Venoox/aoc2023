from collections import defaultdict
from functools import cmp_to_key
from itertools import product

card_power = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

card_power_part2 = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def part1(filename: str):
    hands = []
    with open(filename, "r") as file:
        for line in file.readlines():
            hands.append((line.split(" ")[0], int(line.split(" ")[1])))

    return sum(rank * bid for rank, (hand, bid) in enumerate(sorted(hands, key=cmp_to_key(compare_hands)), start=1))


def part2(filename: str):
    hands = []
    with open(filename, "r") as file:
        for line in file.readlines():
            hands.append((line.split(" ")[0], int(line.split(" ")[1])))

    best_hands = []
    for i, (hand, bid) in enumerate(hands):
        best_hands.append((hand, get_strongest_hand(hand), bid))
    return sum(rank * bid for rank, (hand, _, bid) in enumerate(sorted(best_hands, key=cmp_to_key(compare_hands_part2)), start=1))


def compare_hands(hand1: tuple[str, int], hand2: tuple[str, int]):
    hand1_type = determine_hand_type(hand1[0])
    hand2_type = determine_hand_type(hand2[0])
    if hand1_type != hand2_type:
        return hand1_type - hand2_type
    else:
        for card1, card2 in zip(hand1[0], hand2[0]):
            if card_power[card1] != card_power[card2]:
                return card_power[card1] - card_power[card2]


def compare_hands_part2(hand1: tuple[str, str, int], hand2: tuple[str, str, int]):
    hand1_type = determine_hand_type(hand1[1])
    hand2_type = determine_hand_type(hand2[1])
    if hand1_type != hand2_type:
        return hand1_type - hand2_type
    else:
        for card1, card2 in zip(hand1[0], hand2[0]):
            if card_power_part2[card1] != card_power_part2[card2]:
                return card_power_part2[card1] - card_power_part2[card2]


def determine_hand_type(hand: str):
    labels = defaultdict(int)
    for card in hand:
        labels[card] += 1
    if len(labels) == 1:
        return 7
    if len(labels) == 2:
        if [1, 4] == sorted(labels.values()):
            return 6
        if [2, 3] == sorted(labels.values()):
            return 5
    if len(labels) == 3:
        if [1, 1, 3] == sorted(labels.values()):
            return 4
        if [1, 2, 2] == sorted(labels.values()):
            return 3
    if len(labels) == 4:
        return 2
    if len(labels) == 5:
        return 1


def get_strongest_hand(hand: str):
    jokers = [idx for idx, card in enumerate(hand) if card == "J"]
    if len(jokers) == 0:
        return hand
    joker_combinations = product(card_power.keys(), repeat=len(jokers))
    best_hand = hand
    best_hand_type = determine_hand_type(best_hand)
    for combinations in joker_combinations:
        new_hand = hand
        for combination in combinations:
            new_hand = new_hand.replace("J", combination, 1)
        new_hand_type = determine_hand_type(new_hand)
        if new_hand_type > best_hand_type:
            best_hand = new_hand
            best_hand_type = new_hand_type
    return best_hand


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))