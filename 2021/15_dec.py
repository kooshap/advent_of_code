from heapq import heappush, heappop

f = open("15_dec.txt", "r")

grid = []
for l in f:
    grid.append(list(map(int, list(l.strip()))))

m, n = len(grid), len(grid[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def nei(i, j):
    ret = []
    for di, dj in directions:
        if 0 <= i+di < 5*m and 0 <= j+dj < 5*n:
            ret.append((i+di, j+dj))
    return ret

best = {}

def grid_v(i, j):
    return (grid[i%m][j%n] + i//m + j//n - 1) % 9 + 1

def bfs():
    h = [[0, 0, 0]]
    best[(0, 0)] = 0
    while h:
        risk, i, j = heappop(h)
        for ni, nj in nei(i, j):
            new_risk = risk+grid_v(ni, nj)
            if (ni, nj) not in best or new_risk < best[(ni, nj)]:
                best[(ni, nj)] = new_risk
                if ni == 5*m-1 and nj == 5*n-1:
                    return new_risk
                heappush(h, [new_risk, ni, nj])

print(bfs())
