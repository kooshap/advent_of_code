f = open('in.txt', 'r')
x = y = 0
aim = 0
for line in f:
    c, v = line.strip().split()
    if c == "forward":
        x += int(v)
        y += aim*int(v)
    elif c == "up":
        aim -= int(v)
    else:
        aim += int(v)

print(x*y)

