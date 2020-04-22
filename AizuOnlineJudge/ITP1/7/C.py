r, c = map(int, input().split())

A = []
for _ in range(r):
    a = [int(x) for x in input().split()]
    a.append(sum(a))
    A.append(a)

B = []
for i in range(c + 1):
    b = 0
    for j in range(r):
        b += A[j][i]
    B.append(b)
A.append(B)

for a in A:
    print(*a)