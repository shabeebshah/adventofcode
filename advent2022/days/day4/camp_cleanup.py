def parse_data(filename):
    return open(filename).readlines()


def find_overlaps(data):
    overlaps = 0
    overlaps_2 = 0
    for section in data:
        ranges = []
        elf_a, elf_b = section.split(',')
        for elf in [elf_a, elf_b]:
            elf_min, elf_max = elf.split('-')
            ranges.append(range(int(elf_min), int(elf_max) + 1))
        if any(min(ranges[x]) <= min(ranges[y]) and max(ranges[x]) >= max(ranges[y]) for x, y in ((0, 1), (1, 0))):
            overlaps += 1
        if set(ranges[0]).intersection(set(ranges[1])):
            overlaps_2 += 1

    return overlaps, overlaps_2

print(find_overlaps(parse_data('sections.txt')))

# Dead simple version
# elf_a_min, elf_a_max = elf_a.split('-')
# elf_b_min, elf_b_max = elf_b.split('-')
# elf_a_min = int(elf_a_min)
# elf_a_max = int(elf_a_max)
# elf_b_min = int(elf_b_min)
# elf_b_max = int(elf_b_max)
#
# overlaps += (elf_a_min <= elf_b_min and elf_a_max >= elf_b_max) or (elf_a_min >= elf_b_min and elf_a_max <= elf_b_max)
# first = [i for i in range(elf_a_min, elf_a_max + 1)]
# second = [i for i in range(elf_b_min, elf_b_max + 1)]
# print(set(first), set(second))
# overlaps_2 += len(list(set(first) & set(second))) > 0