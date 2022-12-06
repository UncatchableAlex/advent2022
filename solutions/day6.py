f = open("../inputs/day6.txt").read()
print(min([i for i in range(4, len(f)) if len(set(f[i-4:i])) == 4]))
print(min([i for i in range(14, len(f)) if len(set(f[i-14:i])) == 14]))