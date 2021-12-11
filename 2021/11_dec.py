f = open("11_dec.txt", "r")

grid = []
for l in f:
    grid.append(list(map(int, list(l.strip()))))

m, n = len(grid), len(grid[0])

def flash(i, j):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if 0 <= i+di < m and 0 <= j+dj < n and (di or dj):
                grid[i+di][j+dj] += 1

def round():
    flash_count = 0
    for i in range(m):
        for j in range(n):
            grid[i][j] += 1

    flashed = True
    seen = set()
    while flashed:
        flashed = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 10 and (i, j) not in seen:
                    seen.add((i, j))
                    flash(i, j)
                    flash_count += 1
                    flashed = True
    for i, j in seen:
        grid[i][j] = 0
    return (len(seen))

total_flashes = 0
for i in range(1000):
    flashes = round()
    if flashes == m*n:
        sim_flash_round = i+1
        break
    if i < 100:
        total_flashes += flashes

print("total_flashes:", total_flashes)
print("firt simultaneous round:", sim_flash_round)

