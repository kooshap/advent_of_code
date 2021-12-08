from collections import deque

def overlap(s1, s2):
    ans = 0
    for c in s1:
        if c in s2:
            ans += 1
    return ans 

def sort_s(s):
    return "".join(sorted(list(s)))

d = {2:1, 4:4, 3:7, 7:8}
ans = 0

f = open('8_dec.txt', 'r')
for line in f:
    mapping = {}
    parts = line.strip().split('|')
    inp, out = parts
    out = out.strip().split()
    inp = inp.strip().split()
    out = [sort_s(item) for item in out]
    inp = [sort_s(item) for item in inp]
    
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
    
    cur = 0
    for num in out:
        if num in mapping:
            cur = cur*10 + mapping[num]
        else:
            print("failed")
            break

    ans += cur

print(ans)
