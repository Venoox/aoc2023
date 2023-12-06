import math


def part1(filename: str):
    with open(filename, "r") as file:
        time_section, distance_section = file.read().split("\n")
    times = list(map(int, time_section.split(":")[1].strip().split()))
    distances = list(map(int, distance_section.split(":")[1].strip().split()))
    total_ways = []
    for max_time, record in zip(times, distances):
        min_button_time = 0
        max_button_time = 0
        for button_time in range(1, max_time):
            traveled = (max_time - button_time) * button_time
            if traveled > record:
                min_button_time = button_time
                break
        for button_time in reversed(range(1, max_time)):
            traveled = (max_time - button_time) * button_time
            if traveled > record:
                max_button_time = button_time
                break
        total_ways.append(max_button_time-min_button_time+1)
    return math.prod(total_ways)


def part2(filename: str):
    with open(filename, "r") as file:
        time_section, distance_section = file.read().split("\n")
    max_time = int("".join(time_section.split(":")[1].strip().split()))
    record = int("".join(distance_section.split(":")[1].strip().split()))

    min_button_time = 0
    max_button_time = 0
    for button_time in range(1, max_time):
        traveled = (max_time - button_time) * button_time
        if traveled > record:
            min_button_time = button_time
            break
    for button_time in reversed(range(1, max_time)):
        traveled = (max_time - button_time) * button_time
        if traveled > record:
            max_button_time = button_time
            break
    return max_button_time-min_button_time+1


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
