

def part1(filename: str):
    with open(filename, "r") as file:
        patterns = file.read().split("\n\n")

    horizontal_reflections = 0
    vertical_reflections = 0
    for pattern in patterns:
        pattern = pattern.strip().split("\n")
        rotated_pattern = [''.join(pattern[y][x] for y in reversed(range(0, len(pattern)))) for x in range(0, len(pattern[0]))]
        if (reflection := find_reflection(pattern)) > 0:
            horizontal_reflections += reflection
        elif (reflection := find_reflection(rotated_pattern)) > 0:
            vertical_reflections += reflection

    return vertical_reflections + 100 * horizontal_reflections


def part2(filename: str):
    with open(filename, "r") as file:
        patterns = file.read().split("\n\n")

    horizontal_reflections = 0
    vertical_reflections = 0
    for pattern in patterns:
        pattern = pattern.strip().split("\n")
        rotated_pattern = [''.join(pattern[y][x] for y in reversed(range(0, len(pattern)))) for x in range(0, len(pattern[0]))]
        if (reflection := fix_smudge(pattern)) > 0:
            horizontal_reflections += reflection
        elif (reflection := fix_smudge(rotated_pattern)) > 0:
            vertical_reflections += reflection

    return vertical_reflections + 100 * horizontal_reflections


def fix_smudge(pattern: list[str]):
    for idx, (first, second) in enumerate(zip(pattern, pattern[1:])):
        if (diff := find_diff(first, second)) <= 1:
            curr_offset = 1
            found_reflection = True
            fixed_smudge = diff == 1
            while idx - curr_offset >= 0 and idx + curr_offset + 1 < len(pattern):
                diff = find_diff(pattern[idx - curr_offset], pattern[idx + curr_offset + 1])
                if diff == 1 and not fixed_smudge:
                    fixed_smudge = True
                elif diff > 0:
                    found_reflection = False
                    break
                curr_offset += 1
            if found_reflection and fixed_smudge:
                return idx + 1
    return 0


def find_diff(line1: str, line2: str):
    diff = 0
    for point1, point2 in zip(line1, line2):
        if point1 != point2:
            diff += 1
        if diff > 1:
            return diff
    return diff


def find_reflection(pattern: list[str]):
    for idx, (first, second) in enumerate(zip(pattern, pattern[1:])):
        if first == second:
            curr_offset = 1
            found_reflection = True
            while idx - curr_offset >= 0 and idx + curr_offset + 1 < len(pattern):
                if pattern[idx - curr_offset] != pattern[idx + curr_offset + 1]:
                    found_reflection = False
                    break
                curr_offset += 1
            if found_reflection:
                return idx + 1
    return 0


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
