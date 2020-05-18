# D - .. (Double Dots)

import queue

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

INF = 10 ** 5 + 1
ans = [INF] * N
Q = queue.Queue()
Q.put(0)
ans[0] = 0
while not Q.empty():
    u = Q.get()
    for g in G[u]:
        if ans[g] == INF:
            ans[g] = u + 1
            Q.put(g)

if max(ans) == INF:
    print('No')
else:
    print('Yes')
    for i in range(1, len(ans)):
        print(ans[i])
