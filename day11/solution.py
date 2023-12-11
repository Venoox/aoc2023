from operator import itemgetter
from copy import deepcopy
from itertools import combinations


def part1(filename: str):
    galaxy_coord: list[tuple[int, int]] = []
    with open(filename, "r") as file:
        for y, line in enumerate(file.readlines()):
            galaxy_coord.extend([(x, y) for x, point in enumerate(line.strip()) if point == "#"])
            universe_x_length = len(line.strip())
    universe_y_length = y+1
    galaxy_coord = expand_universe(galaxy_coord, universe_x_length, universe_y_length, 1)
    return sum(abs(x2 - x1) + abs(y2 - y1) for (x1, y1), (x2, y2) in combinations(galaxy_coord, r=2))


def part2(filename: str):
    galaxy_coord: list[tuple[int, int]] = []
    with open(filename, "r") as file:
        for y, line in enumerate(file.readlines()):
            galaxy_coord.extend([(x, y) for x, point in enumerate(line.strip()) if point == "#"])
            universe_x_length = len(line.strip())
    universe_y_length = y + 1
    galaxy_coord = expand_universe(galaxy_coord, universe_x_length, universe_y_length, 1000000-1)
    return sum(abs(x2 - x1) + abs(y2 - y1) for (x1, y1), (x2, y2) in combinations(galaxy_coord, r=2))


def expand_universe(galaxy_coord: list[tuple[int, int]], x_length: int, y_length: int, times: int):
    galaxy_coord = deepcopy(galaxy_coord)
    x_without_galaxies = set(range(0, x_length)) - set(map(itemgetter(0), galaxy_coord))
    y_without_galaxies = set(range(0, y_length)) - set(map(itemgetter(1), galaxy_coord))
    for empty_x in sorted(x_without_galaxies, reverse=True):
        for idx, (x, y) in enumerate(galaxy_coord):
            if x > empty_x:
                galaxy_coord[idx] = (x+times, y)
    for empty_y in sorted(y_without_galaxies, reverse=True):
        for idx, (x, y) in enumerate(galaxy_coord):
            if y > empty_y:
                galaxy_coord[idx] = (x, y+times)
    return galaxy_coord


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
