def part1(filename: str):
    with open(filename, "r") as file:
        histories = file.read().strip().split("\n")
    return sum(get_next_in_seq(list(map(int, history.split()))) for history in histories)


def part2(filename: str):
    with open(filename, "r") as file:
        histories = file.read().strip().split("\n")
    return sum(get_previous_in_seq(list(map(int, history.split()))) for history in histories)


def get_next_in_seq(seq: list[int]):
    if all(d == seq[0] for d in seq):
        return seq[0]
    diff = list(num2 - num1 for (num1, num2) in zip(seq, seq[1:]))
    return seq[-1] + get_next_in_seq(diff)


def get_previous_in_seq(seq: list[int]):
    if all(d == seq[0] for d in seq):
        return seq[0]
    diff = list(num2 - num1 for (num1, num2) in zip(seq, seq[1:]))
    return seq[0] - get_previous_in_seq(diff)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
