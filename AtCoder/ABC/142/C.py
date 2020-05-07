# C - Go to School

N = int(input())
A = [int(a) for a in input().split()]
D = {}
for i in range(N):
    D[i] = A[i]
sort = sorted(D.items(), key=lambda x: x[1])
ans = [i[0] + 1 for i in sort]
print(*ans)
