# B - Greedy Takahashi

A, B, K = map(int, input().split())

if A <= K:
    B = B - min(B, K - A)
    A = 0
else:
    A = A - K

print(A, B)
