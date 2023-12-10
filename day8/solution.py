from math import lcm


def part1(filename: str):
    with open(filename, "r") as file:
        instructions, nodes = file.read().split("\n\n")
    instructions = instructions.strip()
    node_map = {}
    for node in nodes.strip().split("\n"):
        node, instruction = node.split(" = ")
        node_map[node] = (instruction.split(", ")[0].replace("(", ""), instruction.split(", ")[1].replace(")", ""))

    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = node_map[current_node][0]
            if instruction == "R":
                current_node = node_map[current_node][1]
            steps += 1
            if current_node == "ZZZ":
                break
    return steps


def part2(filename: str):
    with open(filename, "r") as file:
        instructions, nodes = file.read().split("\n\n")
    instructions = instructions.strip()
    node_map = {}
    for node in nodes.strip().split("\n"):
        node, instruction = node.split(" = ")
        node_map[node] = (instruction.split(", ")[0].replace("(", ""), instruction.split(", ")[1].replace(")", ""))

    current_nodes = [node for node in node_map.keys() if node.endswith("A")]
    current_nodes_steps = []
    for node in current_nodes:
        current_node = node
        steps = 0
        while not current_node.endswith("Z"):
            for instruction in instructions:
                if instruction == "L":
                    current_node = node_map[current_node][0]
                if instruction == "R":
                    current_node = node_map[current_node][1]
                steps += 1
                if current_node.endswith("Z"):
                    break
        current_nodes_steps.append(steps)
    return lcm(*current_nodes_steps)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
