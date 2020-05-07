# C - Maximal Value

N = int(input())
B = [int(b) for b in input().split()]

A = [float('inf')] * N
for i in range(N - 1):
    A[i + 1] = B[i]
    if B[i] < A[i]:
        A[i] = B[i]

print(sum(A))
