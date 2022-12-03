f = open("../inputs/day1.txt")
# get a list of calories for each elf:
elf_cals_str: [[str]] = [elf.split("\n") for elf in f.read().split("\n\n")]
elf_cals: [[int]] = [[int(cal) for cal in elf] for elf in elf_cals_str]

# sum the calories for the top n elves
def sum_top_elves(n):
    topn = sorted([sum(cals) for cals in elf_cals])[-n:]
    return sum(topn)


print("part1: " + str(sum_top_elves(1)) + "\npart2: " + str(sum_top_elves(3)))