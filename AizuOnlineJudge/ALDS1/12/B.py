INF = float('inf')
N = int(input())
D = [INF] * N
Visited = [False] * N
M = [[INF] * N for _ in range(N)]
for _ in range(N):
    u, k, *cv = map(int, input().split())
    for i in range(0, len(cv), 2):
        c, v = cv[i], cv[i + 1]
        M[u][c] = v

D[0] = 0

while True:
    min_cost = INF
    u = -1
    for i in range(N):
        if not Visited[i] and D[i] < min_cost:
            u = i
            min_cost = D[i]

    if u == -1:
        break

    Visited[u] = True

    for i in range(N):
        if not Visited[i] and M[u][i] != INF and M[u][i] + D[u] < D[i]:
            D[i] = M[u][i] + D[u]

for i, d in enumerate(D):
    print(i, d)