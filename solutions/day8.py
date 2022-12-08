f = [[int(tree) for tree in trees] for trees in open('../inputs/day8.txt').read().splitlines()]
assert len(f[0]) == len(f)
visible = [[0] * len(f[0]) for i in range(0, len(f))]
n = len(f[0])
# part 1:
for i in range(0, n):
    largest = [-1] * 4
    for j in range(0, n):
        visible[i][j] |= f[i][j] > largest[0]
        visible[i][n - j - 1] |= f[i][n - j - 1] > largest[1]
        visible[j][i] |= f[j][i] > largest[2]
        visible[n - j - 1][i] |= f[n - j - 1][i] > largest[3]
        largest = [
            max(largest[0], f[i][j]),
            max(largest[1], f[i][n - j - 1]),
            max(largest[2], f[j][i]),
            max(largest[3], f[n - j - 1][i])
        ]

part1 = sum([sum(row) for row in visible])
print(part1)

# part 2:
view = [[0] * len(f[0]) for i in range(0, len(f))]
for i in range(0, n):
    for j in range(0, n):
        k = j + 1
        while k < n and f[i][k] < f[i][j]:
            k += 1
        total = min(k, n - 1) - j
        k = j - 1
        while k >= 0 and f[i][k] < f[i][j]:
            k -= 1
        total *= (j - max(k, 0))
        k = i + 1
        while k < n and f[k][j] < f[i][j]:
            k += 1
        total *= (min(k, n - 1) - i)
        k = i - 1
        while k >= 0 and f[k][j] < f[i][j]:
            k -= 1
        total *= (i - max(k, 0))
        view[i][j] = total

part2 = max([max(row) for row in view])
print(part2)