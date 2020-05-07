# C - City Savers

N = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]

total = 0
for i in range(N):
    attack = min(A[i], B[i])
    A[i] -= attack
    B[i] -= attack
    total += attack
    if 0 < B[i]:
        attack2 = min(B[i], A[i + 1])
        A[i + 1] -= attack2
        B[i] -= attack2
        total += attack2

print(total)
