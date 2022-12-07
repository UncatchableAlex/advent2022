import re

# delete brackets, spaces. replace empty spots with Xs
def parse_box_row(box):
    temp = re.sub("( ){4}", "X", box)
    return re.sub("[\[\] ]", "", temp).ljust(num_boxes, 'X')


f = open("../inputs/day5.txt").read().splitlines()
# find the bottom layer of boxes
bottom_layer = f.index("") - 1
num_boxes = int(f[bottom_layer].split("   ")[-1])

parsed_box_rows = [parse_box_row(row) for row in f[:bottom_layer]]
# transpose our array of boxes and remove space holders:
boxes = [[box for box in stack if box != 'X'] for stack in list(zip(*parsed_box_rows))]
# we only care about the numbers in the move instructions. Extract those:
moves = [eval(re.sub("\D+", ",", move)[1:]) for move in f[bottom_layer + 2:]]
# part 1:
b = [box.copy() for box in boxes]
for (q, orig, dest) in moves:
    b[dest - 1] = list(reversed(b[orig - 1][:q])) + b[dest - 1]
    b[orig - 1] = b[orig - 1][q:]

print("".join([stack[0] for stack in b]))

#part 2
b = [box.copy() for box in boxes]
for (q, orig, dest) in moves:
    b[dest - 1] = list(b[orig - 1][:q]) + b[dest - 1]
    b[orig - 1] = b[orig - 1][q:]

print("".join([stack[0] for stack in b]))
