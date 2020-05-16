import queue

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t, w = map(int, input().split())
    G[s].append((t, w))
    G[t].append((s, w))

INF = float('inf')

def dfs(s):
    dist = [INF] * N
    Q = queue.Queue()
    Q.put(s)
    dist[s] = 0
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if dist[G[u][i][0]] == INF:
                dist[G[u][i][0]] = dist[u] + G[u][i][1]
                Q.put(G[u][i][0])
    return dist

dist = dfs(0)
idx = dist.index(max(dist))
dist = dfs(idx)
print(max(dist))
