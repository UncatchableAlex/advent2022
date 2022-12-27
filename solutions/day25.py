from functools import reduce

# normal unsigned addition things:
def add(a, b, digits):
    a = [*a.rjust(digits, '0')]
    b = [*b.rjust(digits, '0')]
    c = ['0'] * digits
    res = ['0'] * digits
    dec_map = {'1': 1, '2': 2, '-': -1, '=': -2, '0': 0}
    snafu_map = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
    for i in range(digits - 1, -1, -1):
        col_add = dec_map[a[i]] + dec_map[b[i]] + dec_map[c[i]]
        if -3 < col_add < 3:
            res[i] = snafu_map[col_add]
            continue
        elif i == 0:
            raise 'overflow exception'

        c[i - 1] = '1' if col_add >= 3 else '-'
        res[i] = snafu_map[col_add - 5] if col_add >= 3 else snafu_map[5 + col_add]
    return ''.join(res)

f = open('../inputs/day25.txt').read().splitlines()
part1 = reduce(lambda a, b: add(a, b, 20), f)
print(part1)
