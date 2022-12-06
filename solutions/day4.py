f = [assignment.split(",") for assignment in open("../inputs/day4.txt").read().splitlines()]
f = map(lambda a: [a[0].split("-"), a[1].split("-")], f)
f = list(map(lambda a: [[int(a[0][0]), int(a[0][1])], [int(a[1][0]), int(a[1][1])]], f))
part1 = filter(lambda a: (a[0][0] <= a[1][0] and a[0][1] >= a[1][1]) or (a[0][0] >= a[1][0] and a[0][1] <= a[1][1]), f)
print(len(list(part1)))


def overlap(a):
    overlap1 = (a[0][0] <= a[1][0] <= a[0][1]) or (a[0][0] <= a[1][1] <= a[0][1])
    overlap2 = (a[1][0] <= a[0][0] <= a[1][1]) or (a[1][0] <= a[0][1] <= a[1][1])
    return overlap1 or overlap2


part2 = filter(lambda a: overlap(a), f)
print(len(list(part2)))
