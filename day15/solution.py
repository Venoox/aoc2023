def label_hash(input: str):
    value = 0
    for character in input:
        value = ((value+ord(character)) * 17) % 256
    return value


def part1(filename: str):
    with open(filename, "r") as file:
        init_seq = file.read().strip().split(",")
    return sum(label_hash(step) for step in init_seq)


def part2(filename: str):
    with open(filename, "r") as file:
        init_seq = file.read().strip().split(",")

    boxes: list[list[str]] = [[] for _ in range(256)]
    lenses = {}
    for step in init_seq:
        if "-" in step:
            label = step.split("-")[0]
            box = boxes[label_hash(label)]
            if label in box:
                box.remove(label)
                del lenses[label]
        elif "=" in step:
            label, focal_length = step.split("=")
            box = boxes[label_hash(label)]
            if label not in box:
                box.append(label)
            lenses[label] = int(focal_length)

    focusing_power = 0
    for box_number, box in enumerate(boxes, start=1):
        for slot_number, lens_label in enumerate(box, start=1):
            focusing_power += box_number * slot_number * lenses[lens_label]
    return focusing_power


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))