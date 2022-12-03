from collections import Counter
f = open("../inputs/day3.txt").read().split("\n")

# part 1
compartmentOverlap = [set(sack[:(len(sack) >> 1)]) & set(sack[(len(sack) >> 1):]) for sack in f]
rawOverlapVals = [ord(list(overlap)[0]) for overlap in compartmentOverlap]
part1 = sum([(val - 38 if val < 96 else val - 96) for val in rawOverlapVals])
print(part1)

# part 2:
badgeLetters = [set(f[i]) & set(f[i+1]) & set(f[i+2]) for i in range(0, len(f), 3)]
badgeValues = [ord(list(badgeLetter)[0]) for badgeLetter in badgeLetters]
part2 = sum([(val - 38 if val < 96 else val - 96) for val in badgeValues])
print(part2)