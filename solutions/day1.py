f = open("../inputs/day1.txt")
# get a list of calories for each elf:
elfCalsStr: [[str]] = [elf.split("\n") for elf in f.read().split("\n\n")]
elfCals: [[int]] = [[int(cal) for cal in elf] for elf in elfCalsStr]

# sum the calories for the top n elves
def sumTopElves(n):
    topn = sorted([sum(cals) for cals in elfCals])[-n:]
    return sum(topn)


print("part1: " + str(sumTopElves(1)) + "\npart2: " + str(sumTopElves(3)))