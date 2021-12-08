f = open('sam.txt', 'r')
c = 0
lines = []
for line in f:
    v = line.strip()
    lines.append(v)
    c += 1

n = len(lines[0])
count = [0]*n

def dcount(i, a):
    ans = 0
    for v in a:
        ans += int(v[i])
    return ans

cor, oxr = None, None
ox = list(lines)
co = list(lines)
for i in range(n):
    nox = []
    nco = []
    oxc = dcount(i, ox)
    coc = dcount(i, co)
    print(oxc, coc)
    for v in ox:
        if oxc*2 >= len(ox):
            if v[i] == "1":
                nox.append(v)
        else:
            if v[i] == "0":
                nox.append(v)
    for v in co:
        if coc*2 < len(co):
            if v[i] == "1":
                nco.append(v)
        else:
            if v[i] == "0":
                nco.append(v)
    ox = nox
    co = nco
    print(ox)
    print(co)
    if len(ox) == 1:
        oxr = ox[0]
    if len(co) == 1:
        cor = co[0]

def b_to_i(a):
    ans = 0
    for x in a:
        ans *= 2
        ans += int(x)
    return ans


print(oxr)
print(cor)
print(b_to_i(oxr)*b_to_i(cor))
#gamma = [1 if a >= c//2 else 0 for a in g] 
#epsilon = [0 if a >= c//2 else 1 for a in g]
#print(gamma, b_to_i(gamma))
#print(epsilon, b_to_i(epsilon))
#print(b_to_i(gamma)* b_to_i(epsilon))

