# A - The Number of Even Pairs

import math

N, M = map(int, input().split())

cnt = 0
for n in range(1, N):
    cnt += n
for n in range(1, M):
    cnt += n

print(cnt)
