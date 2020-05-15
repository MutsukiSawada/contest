import queue

V, E = map(int, input().split())

G = [[] for _ in range(V)]
visited = [False] * V
indeg = [0] * V
out = []

for _ in range(E):
    s, t = map(int, input().split())
    G[s].append(t)

for i in range(V):
    for j in range(len(G[i])):
        indeg[G[i][j]] += 1

q = queue.Queue()
for i in range(V):
    if indeg[i] == 0 and not visited[i]:
        q.put(i)
        visited[i] = True
        while not q.empty():
            u = q.get()
            out.append(u)
            for j in range(len(G[u])):
                v = G[u][j]
                indeg[v] -= 1
                if indeg[v] == 0 and not visited[v]:
                    visited[v] = True
                    q.put(v)

for el in out:
    print(el)
