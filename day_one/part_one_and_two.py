from typing import List


def get_input() -> List[str]:
    with open("input.txt") as file:
        return [line.strip() for line in file.readlines()]


def get_weights() -> List[int]:
    weights = []
    current_weight_total = 0
    for line in get_input():
        if line.strip() == "":
            # Empty line, so add total into list and reset for next run
            weights.append(current_weight_total)
            current_weight_total = 0
        else:
            # There is processable content on the line, and it's not empty
            current_weight_total += int(line)

    weights.sort(reverse=True)
    return weights


if __name__ == "__main__":
    elf_weights = get_weights()
    heaviest_elf_weight = elf_weights[0]
    top_three_elfs_combined_weight = 0

    for i in range(0, 3):
        top_three_elfs_combined_weight += elf_weights[i]

    print(f"Heaviest Elf = {heaviest_elf_weight}")
    print(f"Top three heaviest elfs combined = {top_three_elfs_combined_weight}")
