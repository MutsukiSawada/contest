# B - Achieve the Goal

N, K, M = map(int, input().split())
A = [int(a) for a in input().split()]

X = M * N - sum(A)
if X <= 0: X = 0
print(X if X <= K else -1)
