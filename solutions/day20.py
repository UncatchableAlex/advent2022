def shift(ls, indices, gap_closed, gap_made):
    inc = 1 if gap_closed < gap_made else -1
    for i in range(gap_closed, gap_made, inc):
        indices[ls[i + inc]] -= inc
        ls[i] = ls[i + inc]


def decode(encoding, mixes):
    ls = list(encoding)
    indices = {}  # make a dictionary of the indices of each element
    for i in range(len(f)):
        suffix = 'a'  # rename duplicates
        while str(ls[i]) + suffix in indices:
            suffix = chr(ord(suffix) + 1)
        indices[str(ls[i]) + suffix] = i
        ls[i] = str(ls[i]) + suffix
    ordered = list(ls)
    for _ in range(mixes):
        for val in ordered:
            n = int(val[:-1])
            old_index = indices[val]
            # This is the secret sauce. You have to derive this formula to solve this problem.
            # The rest is trivial. It's ALL this:
            new_index = (old_index + n) % (len(ls) - 1)
            shift(ls, indices, old_index, new_index)
            ls[new_index] = val
            indices[val] = new_index
    zero = indices['0a']
    return sum([int(ls[i % len(f)][:-1]) for i in range(zero + 1000, zero + 4000, 1000)])


key = 811589153
f = [int(n) for n in open('../inputs/day20.txt').read().splitlines()]
f2 = [n * key for n in f]
print(decode(f, 1))
print(decode(f2, 10))
