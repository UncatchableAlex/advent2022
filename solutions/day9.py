f = open('../inputs/day9.txt').read().splitlines()
move_knot = {
    'R': lambda k: (k[0] + 1, k[1]),
    'L': lambda k: (k[0] - 1, k[1]),
    'U': lambda k: (k[0], k[1] - 1),
    'D': lambda k: (k[0], k[1] + 1)
}


def step_knots(direction, knots):
    knots[0] = move_knot[direction](knots[0])
    for i in range(0, len(knots) - 1):
        head, tail = knots[i], knots[i + 1]  # do a quick rename to enhance readability
        if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) == 4:  # edge case in part 2
            tail = (tail[0] + 1 if head[0] > tail[0] else tail[0] - 1,
                    tail[1] + 1 if head[1] > tail[1] else tail[1] - 1)
        if head[0] - tail[0] > 1:
            tail = (tail[0] + 1, head[1])
        elif head[0] - tail[0] < -1:
            tail = (tail[0] - 1, head[1])
        if head[1] - tail[1] > 1:
            tail = (head[0], tail[1] + 1)
        elif head[1] - tail[1] < -1:
            tail = (head[0], tail[1] - 1)
        knots[i + 1] = tail


def simulate_n_knots(n, instructions):
    tail_visited = {(0, 0)}
    knots = [(0, 0)] * n
    for instr in instructions:
        steps = int(instr.split(' ')[1])
        for i in range(steps):
            step_knots(instr[0], knots)
            tail_visited.add(knots[-1])
    return tail_visited


print(len(simulate_n_knots(2, f)))  # part 1
print(len(simulate_n_knots(10, f)))  # part 2
