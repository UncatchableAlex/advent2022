# find the value that a given monkey will scream:
def solve_monkey(monkey, solved_monkeys, unsolved_monkeys):
    if monkey in solved_monkeys:
        return solved_monkeys[monkey]
    monkey_math = unsolved_monkeys[monkey].split(' ')
    left = solve_monkey(monkey_math[0], solved_monkeys, unsolved_monkeys)
    right = solve_monkey(monkey_math[2], solved_monkeys, unsolved_monkeys)
    solution = int(eval(str(left) + monkey_math[1] + str(right)))
    solved_monkeys[monkey] = solution
    del unsolved_monkeys[monkey]
    return solution

# find all the monkeys in between two monkeys
def path_to_monkey(curr_monkey, target_monkey, solved_monkeys, unsolved_monkeys):
     if curr_monkey == target_monkey:
         return [target_monkey]
     if curr_monkey in solved_monkeys:
         return None
     monkey_math = unsolved_monkeys[curr_monkey].split(' ')
     left = path_to_monkey(monkey_math[0], target_monkey, solved_monkeys, unsolved_monkeys)
     right = path_to_monkey(monkey_math[2], target_monkey, solved_monkeys, unsolved_monkeys)
     if left is not None:
         return [curr_monkey] + left
     elif right is not None:
         return [curr_monkey] + right
     else:
         return None

# Find the needed call of a variable monkey given that the inputted calls to the equals_monkey
# must be equal.
def solve_variable_monkey(equals_monkey, variable_monkey, solved_monkeys, unsolved_monkeys):
    path = path_to_monkey(equals_monkey, variable_monkey, solved_monkeys, unsolved_monkeys)
    sub_monkeys = unsolved_monkeys[equals_monkey].split(' ')
    invariate_monkey = sub_monkeys[0] if sub_monkeys[0] != path[1] else sub_monkeys[2]
    solve_monkey(equals_monkey, solved_monkeys, dict(unsolved_monkeys))
    val = solved_monkeys[invariate_monkey]
    ops = {
        '/0': lambda val, n: val * n,
        '/2': lambda val, n: n / val,
        '*0': lambda val, n: val / n,
        '*2': lambda val, n: val / n,
        '-0': lambda val, n: val + n,
        '-2': lambda val, n: -1 * (val - n),
        '+0': lambda val, n: val - n,
        '+2': lambda val, n: val - n,
    }
    # The call of each monkey between the equals_monkey and the variable_monkey will be dependent on one sub_monkey
    # whose call is invariate (not determined by anything that we do) and another monkey whose call we
    # do control (with our choice of call for the variable_monkey). All monkeys whose call we do control will exist
    # in the path between the equals_monkey and the variable_monkey. We can find the call of the variable_monkey by
    # performing algebra to calculate the needed call of each sub_monkey whose call we do control (along the path
    # between the equals_monkey and the variable monkey).
    for i in range(1, len(path) - 1):
        sub_monkeys = unsolved_monkeys[path[i]].split(' ')
        op = sub_monkeys[1] # the operation performed on the calls of the two submonkeys
        idx = sub_monkeys.index(path[i + 1]) # the index of the variate monkey in sub_monkeys
        invariate_monkey = sub_monkeys[0] if sub_monkeys[0] != path[i + 1] else sub_monkeys[2]
        val = ops[op + str(idx)](val, solved_monkeys[invariate_monkey]) # perform algebra
    return int(val)

f = open('../inputs/day21.txt').read().splitlines()
solved_monkeys = {n[0]: int(n[1]) for n in [m.split(': ') for m in f] if n[1].isnumeric()}
unsolved_monkeys = {n[0]: n[1] for n in [m.split(': ') for m in f] if not n[1].isnumeric()}
part1 = solve_monkey('root', dict(solved_monkeys), dict(unsolved_monkeys))
part2 = solve_variable_monkey('root', 'humn', solved_monkeys, unsolved_monkeys)
print(part1)
print(part2)
