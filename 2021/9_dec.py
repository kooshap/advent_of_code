from functools import reduce
f = open("9_dec.txt", "r")

grid = []
for l in f:
    s = l.strip()
    row = map(int, list(s))
    grid.append(list(row))

ans = 0
m, n = len(grid), len(grid[0])
for i in range(m):
    for j in range(n):
        lower = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i+di < m and 0 <= j+dj < n:
                if grid[i+di][j+dj] <= grid[i][j]:
                    lower += 1
        if not lower:
            ans += grid[i][j]+1

print(ans)

ans2 = 0

def dfs(i, j):
    s = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= i+di < m and 0 <= j+dj < n:
            if grid[i+di][j+dj] != 9:
                grid[i+di][j+dj] = 9
                s += dfs(i+di, j+dj)
    return s

bs = []
for i in range(m):
    for j in range(n):
        if grid[i][j] != 9:
            grid[i][j] = 9
            bs.append(dfs(i, j))

top3 = sorted(bs)[-3:]
print(reduce((lambda a, b: a*b), top3))
