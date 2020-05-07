# B - Buffet

N = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
C = [int(c) for c in input().split()]

ans = 0
for i in range(N):
    ans += B[A[i] - 1]
    if i == N - 1:
        break
    if A[i] == A[i + 1] - 1:
        ans += C[A[i] - 1]

print(ans)
