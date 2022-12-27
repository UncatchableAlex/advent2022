class BlizzardStateGenerator:
    def __init__(self, f):
        self.translations = {
            '>': lambda n: (n[0], n[1] + 1) if n[1] < len(f[0]) - 2 else (n[0], 1),
            '<': lambda n: (n[0], n[1] - 1) if n[1] > 1 else (n[0], len(f[0]) - 2),
            '^': lambda n: (n[0] - 1, n[1]) if n[0] > 1 else (len(f) - 2, n[1]),
            'v': lambda n: (n[0] + 1, n[1]) if n[0] < len(f) - 2 else (1, n[1]),
        }
        start_state = {(i, j): [f[i][j]] for i in range(len(f)) for j in range(len(f[i])) if f[i][j] in self.translations}
        self.states = [start_state]

    def getstate(self, state):
        while state >= len(self.states):
            new_state = dict()
            for loc, dirs in self.states[-1].items():
                for direction in dirs:
                    new_loc = self.translations[direction](loc)
                    new_state[new_loc] = [direction] if new_loc not in new_state else new_state[new_loc] + [direction]
            self.states.append(new_state)
        return self.states[state]

# in hindsight, dfs may not have been the right call. There are a few problems with doing this recursively. Notice the
# bajillion different parameters that I needed to prevent run-away recursion and cycles. BFS would have had none of
# these issues. Definitely bfs this. Don't be like me.
def dfs(origin, curr, end, minute, generator, dims, max_depth, visited):
    if curr == end:
        return minute
    blizzards = generator.getstate(minute)
    over_blizz = (curr.real, curr.imag) in blizzards
    # these states are prohibited:
    if minute >= max_depth or (minute, curr) in visited:
        return float('inf')
    if origin != curr and (over_blizz or not (0 < curr.real < dims[0] - 1) or not (0 < curr.imag < dims[1] - 1)
                           or (minute >= max_depth)):
        return float('inf')
    visited.add((minute, curr))
    #print(str(curr) + '   ' + str(minute))
    ops = [1, -1, 1j, -1j, 0]
    return min(dfs(origin, neighbor, end, minute + 1, generator, dims, max_depth, visited) for neighbor in (curr + n for n in ops))


f = open('../inputs/day24.txt').read().splitlines()
generator = BlizzardStateGenerator(f)
start, end, limit = complex(0, 1), complex(len(f) - 1, len(f[0]) - 2), 300
part1 = dfs(start, start, end, 0, generator, (len(f), len(f[0])), limit, set())
part2_1 = dfs(end, end, start, part1 + 1, generator, (len(f), len(f[0])), 2 * limit, set())
part2_2 = dfs(start, start, end, part2_1 + 1, generator, (len(f), len(f[0])), 3 * limit, set())
print(part1)
print(part2_2)
