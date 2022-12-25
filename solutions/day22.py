from re import split
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'x y')


def follow_path(board, path):
    coord = Coordinate(x = board[0].index('.'), y = 0)
    facing = 3
    for instr in path:
        facing = (facing + (1 if instr[0] == 'R' else -1)) % 4
        steps = int(instr[1:])
        for _ in range(steps):
            coord = normal_translate(coord, facing) # move forwards
            if coord.x >= len(board[coord.y]) or board[coord.y][coord.x] == ' ': # if we hit white space
                # move backwards one square and then continue moving backwards until we hit white space again
                coord = normal_translate(coord, (facing + 2) % 4)
                prev = coord # save our original location
                while coord.x < len(board[coord.y]) and board[coord.y][coord.x] != ' ':
                    coord = normal_translate(coord, (facing + 2) % 4) # go backwards one
                coord = normal_translate(coord, facing) # move forward one
                if board[coord.y][coord.x] == '#': # if were now on a wall, just go back to prev
                    coord = prev
                    break
            if board[coord.y][coord.x] == '#': # if we're on top of a wall
                coord = normal_translate(coord, (facing + 2) % 4) # move backwards
                break
    return (1000 * (coord.y + 1)) +  (4 * (coord.x + 1)) + facing


def normal_translate(coord, facing):
    # I'm going to be absolutely shameless with object creation in this method, mostly because I think that it
    # makes the code more readable. Also, it runs fast enough as is. I couldn't do the following python dict/lambda
    # switch case trick if I made coordinates mutable.
    translate = {
        0: lambda n: Coordinate(x=(n.x + 1) % len(board[n.y]), y=n.y),
        1: lambda n: Coordinate(x=n.x, y=(n.y + 1) % len(board)),
        2: lambda n: Coordinate(x=(n.x - 1) % len(board[n.y]), y=n.y),
        3: lambda n: Coordinate(x=n.x, y=(n.y - 1) % len(board)),
    }
    return translate[facing](coord)


# I am so sorry
def cube_translate_test(coord, facing):
    if 8 <= coord.x < 12 and coord.y == 0 and facing == 3:
        return Coordinate(x=coord.x - 8, y=4), 1
    elif coord.x == 8 and 0 <= coord.y < 4 and facing == 2:
        return Coordinate(x=4 + coord.y, y=4), 1
    elif coord.x == 11 and 0 <= coord.y < 4 and facing == 0:
        return Coordinate(x=15, y=11-coord.y), 2
    elif 0 <= coord.x < 4 and coord.y == 4 and facing == 3:
        return Coordinate(x=11-coord.x, y=0), 1
    elif 4 <= coord.x < 8 and coord.y == 4 and facing == 3:
        return Coordinate(x=8, y=coord.x - 4), 0
    elif coord.x == 0 and 4 <= coord.y < 8 and facing == 2:
        return Coordinate(x=19 - coord.y, y=11), 3
    elif 0 <= coord.x < 4 and coord.y == 7 and facing == 1:
        return Coordinate(x=11-coord.x,y=11), 3
    elif 4 <= coord.x < 8 and coord.y == 7 and facing == 1:
        return Coordinate(x=8, y=15-coord.x), 0
    elif coord.x == 8 and 8 <= coord.y < 12 and facing == 2:
        return Coordinate(x=15-coord.y, y=7), 3
    elif 8 <= coord.x < 12 and coord.y == 11 and facing == 1:
        return Coordinate(x=11-coord.x,y=7), 3
    elif 12 <= coord.x < 16 and coord.y == 11 and facing == 1:
        return Coordinate(x=0, y=19-coord.x), 0
    elif coord.x == 15 and 8 <= coord.y < 12 and facing == 0:
        return Coordinate(x=11, y=11-coord.y), 2
    elif 12 <= coord.x < 16 and coord.y == 8 and facing == 3:
        return Coordinate(x=11, y=19-coord.x), 2
    elif coord.x == 11 and 4 <= coord.y < 8 and facing == 0:
        return Coordinate(x=19-coord.y, y=8), 1
    else:
        return normal_translate(coord, facing), facing


# so so so sorry
def cube_translate(coord, facing):
    if 50 <= coord.x < 100 and coord.y == 0 and facing == 3: # 0
        return Coordinate(x=0, y=100 + coord.x), 0
    elif coord.x == 50 and 0 <= coord.y < 50 and facing == 2: # 1
        return Coordinate(x=0, y=149 - coord.y), 0
    elif coord.x == 50 and 50 <= coord.y < 100 and facing == 2: # 2
        return Coordinate(x=coord.y - 50, y=100), 1
    elif 0 <= coord.x < 50 and coord.y == 100 and facing == 3: # 2
        return Coordinate(x=50, y=coord.x + 50), 0
    elif coord.x == 0 and 100 <= coord.y < 150 and facing == 2: # 1
        return Coordinate(x=50, y=149-coord.y), 0
    elif coord.x == 0 and 150 <= coord.y < 200 and facing == 2: # 0
        return Coordinate(x=coord.y - 100, y=0), 1
    elif 0 <= coord.x < 50 and coord.y == 199 and facing == 1: # 3
        return Coordinate(x=coord.x + 100, y = 0), 1
    elif coord.x == 49 and 150 <= coord.y < 200 and facing == 0: # 4
        return Coordinate(x=coord.y - 100, y=149), 3
    elif 50 <= coord.x < 100 and coord.y == 149 and facing == 1: # 4
        return Coordinate(x=49, y=coord.x+100), 2
    elif coord.x == 99 and 100 <= coord.y < 150 and facing == 0: # 5
        return Coordinate(x=149, y=149 - coord.y), 2
    elif coord.x == 99 and 50 <= coord.y < 100 and facing == 0: # 6
        return Coordinate(x=coord.y + 50, y=49), 3
    elif 100 <= coord.x < 150 and coord.y == 49 and facing == 1: # 6
        return Coordinate(x=99, y=coord.x - 50), 2
    elif coord.x == 149 and 0 <= coord.y <= 50 and facing == 0: #5
        return Coordinate(x=99, y=149 - coord.y), 2
    elif 100 <= coord.x < 150 and coord.y == 0 and facing == 3: # 3
        return Coordinate(x=coord.x - 100, y=199), 3
    else:
        return normal_translate(coord, facing), facing


def follow_path_cube(board, path, translate):
    coord = Coordinate(x = board[0].index('.'), y = 0)
    facing = 3
    for instr in path:
        facing = (facing + (1 if instr[0] == 'R' else -1)) % 4
        steps = int(instr[1:])
        for _ in range(steps):
            prev = coord
            coord, facing = translate(coord, facing) # move forwards
            if board[coord.y][coord.x] == '#': # if we're on top of a wall
                coord, facing = translate(coord, (facing + 2) % 4) # move backwards
                facing = (facing + 2) % 4
                break
    return (1000 * (coord.y + 1)) +  (4 * (coord.x + 1)) + facing

f = open('../inputs/day22.txt').read().splitlines()
path = split(r'(?<=\d)(?=\D)', f[-1]) # split on every separate instruction
path[0] = 'R' + path[0] # add this first instruction to the first path so we can maintain a loop invariant later
board = f[:-2]
part1 = follow_path(board, path)
print(part1)
part2 = follow_path_cube(board, path, cube_translate)
print(part2)
