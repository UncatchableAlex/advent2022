f = open('../inputs/day7.txt').read().splitlines()
dir_stack = []
dir_dict = {'/': []}
for cmd in f:
    if cmd == '$ ls':
        continue
    elif cmd == '$ cd ..':
        dir_stack.pop()
    elif cmd[:4] == '$ cd':
        dir_stack.append(cmd[5:])
    elif cmd[:3] == 'dir':
        path = '/'.join(dir_stack)
        dir_dict[path + '/' + cmd[4:]] = []
        dir_dict[path].append(path + '/' + cmd[4:])
    # This line must be a file. Add the file's size to the correct path:
    else:
        path = '/'.join(dir_stack)
        dir_dict[path].append(int(cmd.split(' ')[0]))


def dir_size(dir_nm):
    dir_val = dir_dict[dir_nm]
    total = sum([file_size for file_size in dir_val if isinstance(file_size, int)])
    total += sum([dir_size(subdir) for subdir in dir_val if isinstance(subdir, str)])
    dir_dict[dir_nm] = [total]
    return total


# part 1
part1 = sum([dir_size(dir_name) for dir_name in dir_dict.keys() if dir_size(dir_name) <= 100000])
print(part1)

# part 2
space_needed = 30000000 - (70000000 - dir_dict['/'][0])
part2 = min([size[0] for size in dir_dict.values() if size[0] >= space_needed])
print(part2)
