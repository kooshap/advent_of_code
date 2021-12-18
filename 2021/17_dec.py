from collections import deque

f = open("17_dec.txt", "r")

s = f.readline().strip()[13:]
xb, xe = map(int, s.split(", ")[0][2:].split(".."))
yb, ye = map(int, s.split(", ")[1][2:].split(".."))

def good_dx(dx):
    x = 0
    while dx and x <= xe:
        x += dx
        dx -= 1
        if xb <= x <= xe:
            return True
    return False

def good_dy(dy):
    y = 0
    maxy = 0
    while y >= yb:
        if y <= ye:
            return True, maxy
        y += dy
        dy -= 1
        maxy = max(maxy, y)
    return False, 0

def good_dx_dy(dx, dy):
    x = y = 0
    while x <= xe and y >= yb:
        x += dx
        y += dy
        if xb <= x <= xe and yb <= y <= ye:
            return True
        dx = max(0, dx-1)
        dy -= 1
    return False

dx = 1
dx_ans = []
r = good_dx(dx)
while dx <= xe:
    dx += 1
    r = good_dx(dx)
    if r:
        dx_ans.append(dx)

dy = yb
ans1 = 0
dy_ans = []
q = deque()
q.append(True)
while any(q):
    r, maxy = good_dy(dy)
    if r:
        ans1 = max(ans1, maxy)
        dy_ans.append(dy)
    q.append(r)
    if len(q) > 20:
        q.popleft()
    dy += 1

print(ans1)

ans2 = []
for dx in dx_ans:
    for dy in dy_ans:
        if good_dx_dy(dx, dy):
            ans2.append((dx, dy))
print(len(ans2))
