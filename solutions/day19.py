import re


def parse_blueprint(blueprint):
    blueprint += " 0 ore 0 clay 0 obsidian"
    return [int(re.search(r" ([\d]+) ore", blueprint).group(1)), int(re.search(r" ([\d]+) clay", blueprint).group(1)),
            int(re.search(r" ([\d]+) obsidian", blueprint).group(1))]


def build_bot(bots, resources, bp, t, end, i):
    for j in range(len(bp[i])):
        resources[j] -= bp[i][j]
    for j in range(len(bots)):
        resources[j] += bots[j]
    bots[i] += 1
    res = time_step(bots, resources, bp, t + 1, end, [])
    bots[i] -= 1
    for j in range(len(bots)):
        resources[j] -= bots[j]
    for j in range(len(bp[i])):
        resources[j] += bp[i][j]
    return res


def dont_build_bot(bots, resources, bp, t, end, banned_bots):
    for j in range(len(bots)):
        resources[j] += bots[j]
    res = time_step(bots, resources, bp, t + 1, end, banned_bots)
    for j in range(len(bots)):
        resources[j] -= bots[j]
    return res


def could_build_bot(resources, bp, i):
    for j in range(len(bp[i])):
        if resources[j] < bp[i][j]:
            return False
    return True


def should_build_bot(bots, bp, i):
    for j in range(len(bp)):
        if bots[i] <= bp[j][i]:
            return True
    return False


def time_step(bots, resources, bp, t, end, banned_bots):
    if t == end:
        return resources[-1]
    if could_build_bot(resources, bp, -1):
        return build_bot(bots, resources, bp, t, end, -1)
    banned_bots_new = []
    best = 0
    for i in range(len(bp) - 1):
        could_build = could_build_bot(resources, bp, i)
        should_build = should_build_bot(bots, bp, i)
        if could_build:
            banned_bots_new.append(i)
        if could_build and should_build and i not in banned_bots:
            build = build_bot(bots, resources, bp, t, end, i)
            best = max(build, best)
    dont_build = dont_build_bot(bots, resources, bp, t, end, banned_bots_new)
    return max(best, dont_build)


f = [blueprint.split(": ")[1].split(". ") for blueprint in open('../inputs/day19.txt').read().splitlines()]
bps = [[parse_blueprint(recipe) for recipe in bp] for bp in f]
part1 = 0
part2 = 1
for i in range(len(bps)):
    part1 += ((i + 1) * time_step([1, 0, 0, 0], [0, 0, 0, 0], bps[i], 0, 24, []))
    part2 *= (time_step([1, 0, 0, 0], [0, 0, 0, 0], bps[i], 0, 32, []) if i < 3 else 1)
print(part1)
print(part2)
