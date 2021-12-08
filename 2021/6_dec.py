f = open('6_dec.txt', 'r')

nums = list(map(int, f.readline().strip().split(',')))

from functools import lru_cache

@lru_cache(None)
def c_after_d(v, n):
    if v >= n:
        return 1
    return c_after_d(6, n-v-1)+c_after_d(8, n-v-1)

days = 256
ans = 0
for a in nums:
    ans += c_after_d(a, days)

print(ans)

