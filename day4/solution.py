from collections import defaultdict


def solve(filename: str):
    num_of_cards = defaultdict(lambda: 1)
    points_sum = 0
    with open(filename, "r") as file:
        for game_num, line in enumerate(file.readlines(), 1):
            if game_num not in num_of_cards:
                num_of_cards[game_num] = 1
            number_list = line.split(":")[1].split("|")
            matching_numbers = len(set(map(int, number_list[0].strip().split())) & set(map(int, number_list[1].strip().split())))
            if matching_numbers > 0:
                points_sum += 2 ** (matching_numbers-1)
            for i in range(1, matching_numbers+1):
                num_of_cards[game_num+i] += 1*num_of_cards[game_num]

    return points_sum, sum(num_of_cards.values())


if __name__ == "__main__":
    print(solve("input.txt"))
