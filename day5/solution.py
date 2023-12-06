def part1(filename: str):
    with open(filename) as f:
        content = f.read()
    sections = content.split("\n\n")
    seeds = list(map(int, sections[0].split(":")[1].strip().split()))
    maps = []
    for i, section in enumerate(sections[1:]):
        maps.append([])
        for mapping in section.split(":")[1].strip().split("\n"):
            maps[i].append(list(map(int, mapping.split())))

    locations = []
    for seed in seeds:
        input = seed
        for mappings in maps:
            output = None
            for mapping in mappings:
                dest_start, source_start, _range = mapping
                if source_start <= input < source_start + _range:
                    output = dest_start + (input - source_start)
                    break
            if output:
                input = output
        locations.append(input)
    return min(locations)


def part2(filename: str):
    with open(filename) as f:
        content = f.read()
    sections = content.split("\n\n")
    seeds = list(map(int, sections[0].split(":")[1].strip().split()))
    seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
    maps = []
    for i, section in enumerate(sections[1:]):
        maps.append([])
        for mapping in section.split(":")[1].strip().split("\n"):
            maps[i].append(list(map(int, mapping.split())))

    input_ranges = seed_ranges
    for mappings in maps:
        output_ranges: list[tuple[int, int]] = []
        for input_range in input_ranges:
            input_start, input_end = input_range
            found_overlap = False
            for mapping in mappings:
                dest_start, source_start, _range = mapping
                source_end = source_start + _range - 1
                dest_end = dest_start + _range - 1
                if source_start <= input_start and source_end >= input_end:
                    # whole input range is inside the source range
                    output_ranges.append(
                        (dest_start + (input_start - source_start), dest_start + (input_end - source_start)))
                    found_overlap = True
                    break
                elif input_start < source_start <= input_end <= source_end:
                    # left side of the range is outside
                    input_ranges.append((input_start, source_start - 1))
                    output_ranges.append((dest_start, dest_start + (input_end - source_start)))
                    found_overlap = True
                    break
                elif input_end > source_end >= input_start >= source_start:
                    # right side of the range is outside
                    input_ranges.append((source_end + 1, input_end))
                    output_ranges.append((dest_start + (input_start - source_start), dest_end))
                    found_overlap = True
                    break
                elif input_start < source_start and input_end > source_end:
                    input_ranges.append((input_start, source_start - 1))
                    input_ranges.append((source_end + 1, input_end))
                    output_ranges.append((dest_start, dest_end))
                    found_overlap = True
                    break
            if not found_overlap:
                output_ranges.append((input_start, input_end))
        input_ranges = output_ranges
    return min(input_ranges, key=lambda x: x[0])[0]


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
