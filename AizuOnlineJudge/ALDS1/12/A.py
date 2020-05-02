INF = float('inf')
N = int(input())
M = []
D = []
P = []
visited = []
for i in range(N):
    M.append([a if a != -1 else INF for a in map(int, input().split())])
    D.append(INF)
    P.append(-1)
    visited.append(False)

D[0] = 0
P[0] = None

while True:
    min_cost = INF
    u = -1
    for i in range(N):
        if not visited[i] and D[i] < min_cost:
            u = i
            min_cost = D[i]

    if u == -1:
        break

    visited[u] = True

    for i, m in enumerate(M[u]):
        if not visited[i] and m != INF and m < D[i]:
            D[i] = m
            P[i] = u

print(sum(D))