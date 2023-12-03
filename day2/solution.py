available_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def part1(filename: str):
    return sum(int(line.split(":")[0].split(" ")[1]) for line in open(filename, "r").readlines()
               if all(all((int(cubes.strip().split(" ")[0]) <= available_cubes[cubes.strip().split(" ")[1]])
                          for cubes in game_set.split(","))
                      for game_set in line.split(":")[1].split(";")))


def part2(filename: str):
    power = 0
    for line in open(filename, "r").readlines():
        max_red = 0
        max_green = 0
        max_blue = 0
        for game_set in line.split(":")[1].split(";"):
            cubes = game_set.split(",")
            for cube in cubes:
                number, color = cube.strip().split(" ")
                if color == "red":
                    max_red = max(max_red, int(number))
                elif color == "green":
                    max_green = max(max_green, int(number))
                elif color == "blue":
                    max_blue = max(max_blue, int(number))
        power += max_red * max_green * max_blue
    return power


if __name__ == '__main__':
    print(part1("input.txt"))
    print(part2("input.txt"))

            