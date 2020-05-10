# D - Banned K

from collections import Counter

N = int(input())
A = [int(a) for a in input().split()]

counter = Counter(A)
total = 0
for v in counter.values():
    total += v * (v - 1) // 2

for i in range(N):
    print(total - (counter[A[i]] - 1))
