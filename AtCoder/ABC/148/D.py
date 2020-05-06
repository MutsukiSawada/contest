# D - Brick Break

N = int(input())
A = [int(a) for a in input().split()]

ls = []
i = 1
for j in range(N):
    if A[j] == i:
        ls.append(A[j])
        i += 1

print(len(A) - len(ls) if 0 < len(ls) else -1)
