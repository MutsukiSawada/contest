N = int(input())
G = [[0] * N for _ in range(N)]

for _ in range(N):
    u, n, *K = map(int, input().split())
    u -= 1
    for k in K:
        k -= 1
        G[u][k] = 1

for g in G:
    print(*g)
