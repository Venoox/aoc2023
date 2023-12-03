import re


def part1(filename: str):
    return sum(list(map(lambda line: 10 * next(int(ch) for ch in line if ch.isdigit()) + next(int(ch) for ch in reversed(line) if ch.isdigit()),
                        open(filename, "r").readlines())))


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

r_first = f"({'|'.join(numbers.keys())})"
r_last = f"({'|'.join(x[::-1] for x in numbers.keys())})"


def part2(filename: str):
    return sum(10 * numbers[re.findall(r_first, line)[0]] + numbers[re.findall(r_last, line[::-1])[0][::-1]]
               for line in open(filename, "r").readlines())


if __name__ == '__main__':
    print(part1("input.txt"))
    print(part2("input.txt"))
