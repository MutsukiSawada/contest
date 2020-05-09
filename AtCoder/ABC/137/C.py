# C - Green Bin

from collections import Counter

N = int(input())
S = [str(input()) for _ in range(N)]
for i in range(N):
    S[i] = ''.join(sorted([s for s in S[i]]))
counter = Counter(S)
ans = 0
for i in counter.values():
    tmp = 0
    for j in range(1, i):
        tmp += j
    ans += tmp

print(ans)
