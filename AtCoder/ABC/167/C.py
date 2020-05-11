# C - Skill Up

N, M, X = map(int, input().split())
C, A = [], []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

costs = []
def f(i, cost, points):
    if X <= min(points):
        costs.append(cost)
        return
    if N <= i:
        return
    f(i + 1, cost, points)
    tmp = [p for p in points]
    for j in range(M):
        tmp[j] += A[i][j]
    f(i + 1, cost + C[i], tmp)

f(0, 0, [0] * M)
print(min(costs) if len(costs) != 0 else -1)