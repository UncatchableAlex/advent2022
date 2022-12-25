from itertools import product


def get_neighbors(drop):
    neighbor_ranges = [range(n - 1, n + 2) for n in drop]
    # all drops in the cartesian product of the neighbor ranges with manhattan distance of 1:
    return [n for n in product(*neighbor_ranges) if sum([abs(n[i] - drop[i]) for i in range(len(n))]) == 1]


def get_surface_area(drops):
    surface_area = 0
    drops_set = set(drops)
    for drop in f:
        surface_area += len([n for n in get_neighbors(drop) if n not in drops_set])
    return surface_area

# For part 2, my genius idea is to do bfs of all open space around the drop (call this set A), take the set difference
# between the entire search space and A (call this result B), and then feeding B into get_surface_area. This isn't going
# to be particularly memory friendly, but I'm not actually sure that there is a better way.
def fill_cavities(drops):
    # I'm going to calculate the search space in an interesting way. The following piece of code is agnostic to the
    # dimension of each drop in drops. After all, for all we know, these could be 18-dimensional drops. We must stay
    # prepared. What the following method lacks in speed, it makes up for in awesomeness.
    corner = [max([drop[i] for drop in drops]) + 2 for i in range(len(drops[0]))]
    ranges = [range(-1, n) for n in corner]
    omega = set(product(*ranges))
    queue = {tuple([-1] * len(drops[0]))}
    drops_set = set(drops)
    visited = set()
    while len(queue) > 0:
        curr = queue.pop()
        for neighbor in get_neighbors(curr):
            if (neighbor not in drops_set) and (neighbor in omega) and (neighbor not in visited):
                queue.add(neighbor)
        visited.add(curr)
    return list(omega - visited)


f = [eval(line) for line in open('../inputs/day18.txt').read().splitlines()]
part1 = get_surface_area(f)
part2 = get_surface_area(fill_cavities(f))
print(part1)
print(part2)
