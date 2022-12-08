f = open('../inputs/day7.txt').read().splitlines()
dir_stack = ['/']
dir_dict = {'/': 0}
for cmd in f[1:]:
    if cmd == '$ cd ..':
        dir_dict[dir_stack[-2]] += dir_dict[dir_stack.pop()]
    elif cmd[:4] == '$ cd':
        dir_stack.append(dir_stack[-1] + '/' + cmd[5:])
    elif cmd[:3] == 'dir':
        # initialize a new directory in our map
        dir_dict[dir_stack[-1] + '/' + cmd[4:]] = 0
    elif cmd != '$ ls':
        # This line must be a file. Add the file's size to the correct path:
        dir_dict[dir_stack[-1]] += int(cmd.split(' ')[0])

while len(dir_stack) > 1:
    dir_dict[dir_stack[-2]] += dir_dict[dir_stack.pop()]

# part 1
part1 = sum([dir_size for dir_size in dir_dict.values() if dir_size <= 100000])
print(part1)

# part 2
space_needed = 30000000 - (70000000 - dir_dict['/'])
part2 = min([size for size in dir_dict.values() if size >= space_needed])
print(part2)
