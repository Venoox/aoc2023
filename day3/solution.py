from collections import defaultdict


def solve(filename: str):
    schematic: list[str] = []
    with open(filename, "r") as file:
        for y, line in enumerate(file.readlines()):
            schematic.append(line.strip())

    sum_of_parts = 0
    potential_gears: dict[tuple[int, int], list[int]] = defaultdict(list)
    for y, row in enumerate(schematic):
        start_of_number = None
        x = 0
        while x <= len(row):
            if x < len(row) and row[x].isdigit() and start_of_number is None:
                start_of_number = x
            if (x == len(row) or not row[x].isdigit()) and start_of_number is not None:
                end_of_number = x - 1
                part_number = int("".join(row[start_of_number:end_of_number + 1]))
                # check if any symbol is around the number
                if check_for_symbol(schematic, y, start_of_number, end_of_number):
                    sum_of_parts += part_number
                # check for * around the number
                gear_coordinates = get_symbol_coordinates(schematic, y, start_of_number, end_of_number, "*")
                for gear in gear_coordinates:
                    potential_gears[gear].append(part_number)
                start_of_number = None
                x = end_of_number
            x += 1

    sum_of_gear_ratio = sum(gears[0]*gears[1] for gears in potential_gears.values() if len(gears) == 2)
    return sum_of_parts, sum_of_gear_ratio


def get_symbol_coordinates(schematic: list[str], y: int, x_start: int, x_stop: int, symbol="*"):
    coordinates: set[tuple[int, int]] = set()
    max_x = len(schematic[0])
    max_y = len(schematic)
    for _y in range(max(0, y-1), min(max_y, y+2)):
        for _x in range(max(0, x_start-1), min(max_x, x_stop+2)):
            if schematic[_y][_x] == symbol:
                coordinates.add((_y, _x))
    # if y > 0:
    #     # check top row
    #     coordinates = coordinates.union((y-1, x) for x in range(max(0, x_start-1), min(x_stop + 2, max_x)) if schematic[y-1][x] == symbol)
    # if y < len(schematic) - 1:
    #     # check bottom row
    #     coordinates = coordinates.union((y+1, x) for x in range(max(0, x_start-1), min(x_stop + 2, max_x)) if schematic[y+1][x] == symbol)
    # # left
    # if x_start > 0 and schematic[y][x_start - 1] == symbol:
    #     coordinates.add((y, x_start - 1))
    # # right
    # if x_stop < max_x - 1 and schematic[y][x_stop + 1] == symbol:
    #     coordinates.add((y, x_stop + 1))
    return coordinates


def check_for_symbol(schematic: list[str], y: int, x_start: int, x_stop: int):
    max_x = len(schematic[0])
    max_y = len(schematic)
    for _y in range(max(0, y-1), min(max_y, y+2)):
        for _x in range(max(0, x_start-1), min(max_x, x_stop+2)):
            if is_symbol(schematic[_y][_x]):
                return True
    return False
    # if y > 0:
    #     # check top row
    #     if any(is_symbol(item) for item in schematic[y - 1][max(0, x_start-1):min(x_stop + 2, max_x)]):
    #         return True
    # if y < len(schematic) - 1:
    #     # check bottom row
    #     if any(is_symbol(item) for item in schematic[y + 1][max(0, x_start-1):min(x_stop + 2, max_x)]):
    #         return True
    # if x_start > 0 and is_symbol(schematic[y][x_start - 1]):
    #     return True
    # if x_stop < max_x - 1 and is_symbol(schematic[y][x_stop + 1]):
    #     return True
    # return False


def is_symbol(item: str):
    return not item.isdigit() and item != "."


if __name__ == '__main__':
    print(solve("input.txt"))
