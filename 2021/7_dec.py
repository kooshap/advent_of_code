f = open('7_dec.txt', 'r')

nums = list(map(int, f.readline().strip().split(',')))

b, e = min(nums), max(nums)
n = len(nums)
ans = float('inf')

def cost(a, b):
    d = abs(a-b)
    return d*(d+1)//2

for i in range(b, e+1):
    r = sum([cost(i, x) for x in nums])
    ans = min(ans, r)

print(ans)
