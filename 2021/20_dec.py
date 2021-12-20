f = open("20_dec.txt", "r")

alg = [] 

for l in f:
    if not l.strip():
        break
    alg.extend(list(l.strip()))

inp = []
for l in f:
    inp.append(list(l.strip()))

def val(i, j, inp, round_idx):
    m, n = len(inp), len(inp[0])
    if 0 <= i < m and 0 <= j < n:
        return inp[i][j]
    return "." if alg[0] == "." or round_idx % 2 == 0 else "#"

def calc(i, j, inp, round_idx):
    ans = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            v = val(i+di, j+dj, inp, round_idx)
            ans = ans*2 + (1 if v == "#" else 0)
    return alg[ans]

def enhance(inp, round_idx):
    m, n = len(inp), len(inp[0])
    out = []
    for i in range(-2, m+2):
        row = []
        for j in range(-2, n+2):
            row.append(calc(i, j, inp, round_idx))
        out.append(row)
    return out

e = inp
rounds = 50
for i in range(rounds):
    e = enhance(e, i)
print(sum([1 if cell == "#" else 0 for row in e[rounds:-rounds] for cell in row[rounds:-rounds]]))

