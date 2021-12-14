from collections import Counter
from functools import lru_cache

f = open("14_dec.txt", "r")

p = f.readline().strip()
f.readline()

d = {}
for line in f:
    k, v = line.strip().split(" -> ")
    d[k] = v

def ic(c):
    return ord(c)-ord("A")

@lru_cache(None)
def res(s, r):
    ans = [0]*26
    if r == 0:
        for c in s:
            ans[ic(c)] += 1
        return ans
    for i in range(len(s)-1):
        part = s[i:i+2]
        ans[ic(d[part])] -= 1
        sub = res(s[i]+d[part], r-1)
        for j, v in enumerate(sub):
            ans[j] += v
        sub = res(d[part]+s[i+1], r-1)
        for j, v in enumerate(sub):
            ans[j] += v
    for c in s[1:-1]:
        ans[ic(c)] -= 1
    return ans

r = res(p, 40)
r = [v for v in r if v]
print(r)
print(max(r), min(r), max(r)-min(r))
