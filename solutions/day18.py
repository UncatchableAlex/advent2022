from functools import reduce
f = [eval(line) for line in open('../inputs/day18.txt').read().splitlines()]


def get_surface_area(drops):
    # get a list of dictionaries to organize the input by each axis.
    # ie the first dictionary maps the first axis to a set of coordinates.
    dicts = [{drop[i]: set() for drop in drops} for i in range(len(drops[0]))]
    for i in range(len(f[0])):
        for drop in f:
            dicts[i][drop[i]].add(drop)

    matching_sides = 0
    for drop in f:
        for i in range(len(drops[0])):
            possible_matches = set(dicts[i][drop[i] - 1]) if (drop[i] - 1 in dicts[i]) else set()
            possible_matches |= dicts[i][drop[i] + 1] if (drop[i] + 1 in dicts[i]) else set()
            for j in range(len(drops[0])):
                if j != i:
                    possible_matches &= dicts[j][drop[j]] if (drop[j] in dicts[j]) else set()
            if len(possible_matches) > 0:
                matching_sides += len(possible_matches)
    return (len(drops) * 6) - matching_sides


def fill_cavities(drops):
    #corner = [max([drop[i] for drop in drops]) for i in range(len(drops[0]))]
    corner = [4, 4, 4]
    corner_product = reduce(lambda a, b: a * b, corner)
    coords = []
    for i in range(corner_product):
        j = i
        coord = []
        for k in range(len(corner)):
            coord.append(j % (corner[k] ** (k + 1)))
            j = int(j / (corner[k] ** (k + 1)))
        coords.append(coord)
    #filled_drop = [[int(j%(corner[i]**i)) for i in range(len(corner))] for j in range(corner_product)]
    print(coords)




#print(get_surface_area(f))
fill_cavities(f)


