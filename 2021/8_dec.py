f = open('8_dec.txt', 'r')

from collections import defaultdict
from collections import deque

d = {2:1, 4:4, 3:7, 7:8}
ans = ans2 = 0

def overlap(s1, s2):
    ans = 0
    for c in s1:
        if c in s2:
            ans += 1
    return ans 

mat = [[0]*10 for _ in range(10)]
mat[1][3] = 2
mat[3][1] = 2
mat[2][5] = 3
mat[5][2] = 3
mat[6][7] = 2
mat[7][6] = 2
mat[6][4] = 3
mat[4][6] = 3
mat[6][1] = 1
mat[1][6] = 1
mat[5][0] = 4
mat[0][5] = 4

def sort_s(s):
    return "".join(sorted(list(s)))

for line in f:
    mapping = {}
    parts = line.strip().split('|')
    inp, out = parts
    out = out.strip().split()
    inp = inp.strip().split()
    print(out)
    out = [sort_s(item) for item in out]
    inp = map(sort_s, inp)
    
    q = deque()
    q.extend(inp)
    q.extend(out)
    while q:
        code = q.popleft()
        l = len(code)
        if l in d:
            mapping[code] = d[l]
        for k, v in list(mapping.items()):
            if l == 5:
                if v == 1 and overlap(code, k) == 2:
                    mapping[code] = 3
                if v == 7 and overlap(code, k) == 3:
                    mapping[code] = 3
                if v == 4 and overlap(code, k) == 2:
                    mapping[code] = 2
                if v == 6 and overlap(code, k) == 5:
                    mapping[code] = 5
            if l == 6:
                if v == 1 and overlap(code, k) == 1:
                    mapping[code] = 6
                if v == 4 and overlap(code, k) == 4:
                    mapping[code] = 9
                if v == 5 and overlap(code, k) == 4:
                    mapping[code] = 0

        if code not in mapping:
            q.append(code)
    
    print(mapping)
    cur = 0
    for num in out:
        if num in mapping:
            cur = cur*10 + mapping[num]
        else:
            print("failed")
            break

    print(list(out))
    print(cur)
    ans2 += cur

print(ans2)
