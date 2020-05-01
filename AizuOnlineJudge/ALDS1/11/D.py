import queue

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

group = [0] * N
group_id = 1
que = queue.Queue()

for i in range(N):
    if group[i] != 0:
        continue
    group[i] = group_id
    que.put(G[i])
    while not que.empty():
        q = que.get()
        for j in q:
            if group[j] == 0:
                que.put(G[j])
                group[j] = group_id
    group_id += 1

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    if group[s] == group[t]:
        print('yes')
    else:
        print('no')
