f = open("../inputs/day1.txt")
food = [elf.split("\n") for elf in [elf for elf in f.read().split("\n\n")]]
cals = [[int(cal) for cal in elf] for elf in food]
def part1():
    return max([sum(elf) for elf in cals])

def part2():
    elvesByCals = [sum(elf) for elf in cals]
    elvesByCals.sort(reverse=True)
    return elvesByCals[0] + elvesByCals[1] + elvesByCals[2]

print("part1: " + str(part1()))
print("part2: " + str(part2()))

