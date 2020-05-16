import sys

sys.setrecursionlimit(10**6)

INF = 100000 + 1
V, E = map(int, input().split())
G = [[] * V for _ in range(V)]
visited = [False] * V
prenum = [INF] * V
parent = [INF] * V
lowest = [INF] * V
timer = 1

for _ in range(E):
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

def dfs(cur, prv):
    global timer
    prenum[cur] = lowest[cur] = timer
    timer += 1
    visited[cur] = True
    for nxt in G[cur]:
        if not visited[nxt]:
            parent[nxt] = cur
            dfs(nxt, cur)
            lowest[cur] = min(lowest[cur], lowest[nxt])
        elif nxt != prv:
            lowest[cur] = min(lowest[cur], prenum[nxt])

dfs(0, -1)

np = 0
ap = []
for i in range(V):
    p = parent[i]
    if p == 0:
        np += 1
    elif p != INF and prenum[p] <= lowest[i]:
        ap.append(p)

if np > 1:
    ap.insert(0, 0)

for ans in sorted(set(ap)):
    print(ans)
