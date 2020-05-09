# D - Triangles

from bisect import bisect_left

N = int(input())
L = sorted([int(l) for l in input().split()])

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        cnt += bisect_left(L, L[i] + L[j]) - (j + 1)

print(cnt)
