from enum import Enum
import sys

sys.setrecursionlimit(5000)


class Point:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


def part1(filename: str):
    with open(filename, "r") as file:
        layout = file.read().strip().split("\n")

    curr = Point(0, 0)
    direction = Direction.RIGHT
    energized = [[[] for _ in range(len(layout[0]))] for _ in range(len(layout))]
    step(curr, direction, layout, energized)
    return sum(sum(len(tile) > 0 for tile in row) for row in energized)


def part2(filename: str):
    with open(filename, "r") as file:
        layout = file.read().strip().split("\n")

    max_energized_tiles = 0

    for x in range(0, len(layout[0])):
        for y in (0, len(layout) - 1):
            for direction in Direction:
                curr = Point(x, y)
                energized = [[[] for _ in range(len(layout[0]))] for _ in range(len(layout))]
                step(curr, direction, layout, energized)
                energized_tiles = sum(sum(len(tile) > 0 for tile in row) for row in energized)
                if energized_tiles > max_energized_tiles:
                    max_energized_tiles = energized_tiles

    for y in range(0, len(layout)):
        for x in (0, len(layout[0]) - 1):
            for direction in Direction:
                curr = Point(x, y)
                energized = [[[] for _ in range(len(layout[0]))] for _ in range(len(layout))]
                step(curr, direction, layout, energized)
                energized_tiles = sum(sum(len(tile) > 0 for tile in row) for row in energized)
                if energized_tiles > max_energized_tiles:
                    max_energized_tiles = energized_tiles

    return max_energized_tiles


def step(curr: Point, direction: Direction, layout: list[str], energized: list[list[list[int]]]):
    if curr.y < 0 or curr.y >= len(layout):
        return
    if curr.x < 0 or curr.x >= len(layout[0]):
        return
    if direction.value in energized[curr.y][curr.x]:
        return
    energized[curr.y][curr.x].append(direction.value)
    tile = layout[curr.y][curr.x]
    if tile == ".":
        if direction == Direction.RIGHT:
            curr.x += 1
        elif direction == Direction.LEFT:
            curr.x -= 1
        elif direction == Direction.UP:
            curr.y -= 1
        elif direction == Direction.DOWN:
            curr.y += 1
    elif tile == "\\":
        if direction == Direction.RIGHT:
            curr.y += 1
            direction = Direction.DOWN
        elif direction == Direction.LEFT:
            curr.y -= 1
            direction = Direction.UP
        elif direction == Direction.UP:
            curr.x -= 1
            direction = Direction.LEFT
        elif direction == Direction.DOWN:
            curr.x += 1
            direction = Direction.RIGHT
    elif tile == "/":
        if direction == Direction.RIGHT:
            curr.y -= 1
            direction = Direction.UP
        elif direction == Direction.LEFT:
            curr.y += 1
            direction = Direction.DOWN
        elif direction == Direction.UP:
            curr.x += 1
            direction = Direction.RIGHT
        elif direction == Direction.DOWN:
            curr.x -= 1
            direction = Direction.LEFT
    elif tile == "-":
        if direction == Direction.RIGHT:
            curr.x += 1
        elif direction == Direction.LEFT:
            curr.x -= 1
        elif direction == Direction.UP or direction == Direction.DOWN:
            step(Point(curr.x + 1, curr.y), Direction.RIGHT, layout, energized)
            step(Point(curr.x - 1, curr.y), Direction.LEFT, layout, energized)
            return
    elif tile == "|":
        if direction == Direction.DOWN:
            curr.y += 1
        elif direction == Direction.UP:
            curr.y -= 1
        elif direction == Direction.LEFT or direction == Direction.RIGHT:
            step(Point(curr.x, curr.y + 1), Direction.DOWN, layout, energized)
            step(Point(curr.x, curr.y - 1), Direction.UP, layout, energized)
            return
    step(Point(curr.x, curr.y), Direction(direction), layout, energized)


def print_layout(layout: list[str]):
    for row in layout:
        print(row)
    print()


def print_energized(energized: list[list[list[int]]]):
    for row in energized:
        for tile in row:
            if len(tile) > 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
