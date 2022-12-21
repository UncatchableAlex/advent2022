f = open('../inputs/day10_test.txt').read().splitlines()
reg = 1
t = 0
score = 0
last = 0
for line in f:
    if line == "noop":
        t += 1
        last = 0
        continue
    modval = (t - 20) % 40
    if modval == 1:
        score += (reg - last) * (t - modval)
        print((reg - last) * (t - modval))
    if modval == 0:
        score += (reg * t)
        print(reg * t)
    last = int(line.split(" ")[1])
    reg += last
    t += 2
print(score)

