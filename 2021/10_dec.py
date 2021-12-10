f = open("10_dec.txt", "r")

penalty = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

match = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

ans = 0
scores = []
for l in f:
    s = []
    p = 0
    for c in l.strip():
        if c in match.keys():
            if not s or s[-1] != match[c]:
                ans += penalty[c]
                p = 1
                break
            else:
                s.pop()
        else:
            s.append(c)
    if not p and s:
        cur_score = 0
        while s:
            cur_score = cur_score*5 + score[s.pop()]
        scores.append(cur_score)

print(ans)
scores.sort()
print(scores[len(scores)//2])

