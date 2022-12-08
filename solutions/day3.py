f = open("../inputs/day3.txt").read().splitlines()

# part 1
compartment_overlap = [set(sack[:(len(sack) >> 1)]) & set(sack[(len(sack) >> 1):]) for sack in f]
raw_overlap_vals = [ord(list(overlap)[0]) for overlap in compartment_overlap]
part1 = sum([(val - 38 if val < 96 else val - 96) for val in raw_overlap_vals])
print(part1)

# part 2:
badge_letters = [set(f[i]) & set(f[i + 1]) & set(f[i + 2]) for i in range(0, len(f), 3)]
badge_values = [ord(list(badgeLetter)[0]) for badgeLetter in badge_letters]
part2 = sum([(val - 38 if val < 96 else val - 96) for val in badge_values])
print(part2)
