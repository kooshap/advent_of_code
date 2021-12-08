f = open("in.txt", "r")

seq = list(map(int, f.readline().split(',')))
f.readline()

i = 0
tables = []
for line in f:
    l = line.strip()
    if l:
        if i % 5 == 0:
            tables.append([])
        tables[i//5].append(list(map(int, l.split())))
        i += 1

def bingo(t, nums):
    for row in t:
        if all([n in nums for n in row]):
            return True

    for j in range(5):
        if all([t[i][j] in nums for i in range(5)]):
            return True

    return False

def score(t, s):
    print(t, s)
    ans = 0
    for row in t:
        for c in row:
            if c not in s:
                ans += c
    return ans*s[-1]

def check_bingo():
    lt = len(tables)
    w = 0
    winners = set()
    for i in range(len(seq)):
        for k, t in enumerate(tables):
            if k not in winners:
                if bingo(t, set(seq[:i+1])):
                    winners.add(k)
                    w += 1
                    if w == lt:
                        return score(t, seq[:i+1])

print(check_bingo())
	
	
