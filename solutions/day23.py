from itertools import product
from functools import reduce


def get_neighbors(elf):
    neighbor_ranges = [range(n - 1, n + 2) for n in elf]
    # all elves in the cartesian product of neighbor_ranges that aren't the elf itself:
    return [n for n in product(*neighbor_ranges) if n != elf]


def move_elves(elf_dict, max_rounds):
    # im not really sure how to abstract elf planning priorities into n-dimensions, so it will stay 2d for now.   :(
    priorities = [
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)],
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)]
    ]
    elves = dict(elf_dict)
    elf_locs = set(elves.values())
    elf_plans = dict()
    rounds = 0
    # no do while loop in Python. We must suffer
    while True:
        rounds += 1
        for id, loc in elves.items():
            if not any(x in elf_locs for x in get_neighbors(loc)): # continue if this elf has no neighbors
                continue
            for priority in priorities:
                # for practice, I will assume that I don't know how many dimensions the elves are moving in.
                # apply the translations given by priority to find the locations that must be free for the elf to plan
                # on moving in that direction:
                priority_neighbors = [tuple(loc[i] + p[i] for i in range(len(loc))) for p in priority]
                if all(pn not in elf_locs for pn in priority_neighbors):
                    # find the square that we plan to move to.
                    move_square = tuple(sum(row) // len(row) for row in list(zip(*priority_neighbors)))
                    elf_plans[move_square] = [id] if move_square not in elf_plans else elf_plans[move_square] + [id]
                    break
        for loc, ids in elf_plans.items():
            if len(ids) == 1:
                elves[ids[0]] = loc
        if len(elf_plans) == 0 or rounds >= max_rounds: # termination condition for our while loop
            break
        priorities.append(priorities.pop(0)) # rotate the priority list
        elf_locs = set(elves.values())
        elf_plans = dict()
    some_loc = list(elf_locs)[0]
    dims = [(max([loc[i] for loc in elf_locs]) - min([loc[i] for loc in elf_locs])) + 1 for i in range(len(some_loc))]
    return reduce(lambda a, b: a * b, dims) - len(elves), rounds


f = open('../inputs/day23.txt').read().splitlines()
elf_locs = [(i, j) for i in range(len(f)) for j, x in enumerate(f[i]) if x == '#']
elves = {i: n for i, n in enumerate(elf_locs)} # we're going to do this with dicts because resizing 2d arrays is hard
part1 = move_elves(elves, 10)
print(part1)
part2 = move_elves(elves, float('inf'))
print(part2)
