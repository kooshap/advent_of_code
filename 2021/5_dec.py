f = open("5_dec.txt", "r")
ans = 0
grid = {}

def test(x, y):
    ans = 0
    if (x, y) in grid:
        grid[(x, y)] += 1
        if grid[(x, y)] == 2:
            ans += 1
    else:
        grid[(x, y)] = 1
    return ans

for line in f:
    points = line.strip().split(" -> ")
    print(points)
    p0 = list(map(int, points[0].split(",")))
    p1 = list(map(int, points[1].split(",")))
    if p0[0] == p1[0]:
        x = p0[0]
        for y in range(min(p0[1], p1[1]), max(p0[1], p1[1])+1):
            ans += test(x, y)
    elif p0[1] == p1[1]:
        y = p0[1]
        for x in range(min(p0[0], p1[0]), max(p0[0], p1[0])+1):
            ans += test(x, y)
    else:
        xd = 1 if p0[0] < p1[0] else -1
        xr = range(p0[0], p1[0]+xd, xd)
        yd = 1 if p0[1] < p1[1] else -1
        yr = range(p0[1], p1[1]+yd, yd)
        for x, y in zip(xr, yr):
            ans += test(x, y)

print(ans)
