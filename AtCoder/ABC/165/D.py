# D - Floor Function

from math import floor

A, B, N = map(int, input().split())

if B <= N:
    mx = floor(A * (B - 1) / B) - A * floor((B - 1) / B)
else:
    mx = floor(A * N / B) - A * floor(N / B)

print(mx)
