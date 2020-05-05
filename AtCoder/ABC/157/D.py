# D - Friend Suggestions

from queue import Queue

N, M, K = map(int, input().split())

friends =  [(i, []) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    friends[a][1].append(b)
    friends[b][1].append(a)

blocks = [(i, []) for i in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    blocks[c][1].append(d)
    blocks[d][1].append(c)

Q = Queue()
visited = [False] * N
group = [0] * N
for i in range(N):
    if visited[i]:
        continue
    Q.put(friends[i])
    visited[i] = True
    while not Q.empty():
        q = Q.get()
        group[q[0]] = i
        for j in q[1]:
            if not visited[j]:
                visited[j] = True
                Q.put(friends[j])

cnt = {}
for num in group:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

ans = [0] * N
for i in range(N):
    ans[i] = cnt[group[i]] - len(friends[i][1]) - 1
    for block in blocks[i][1]:
        if group[i] == group[block]:
            ans[i] -= 1

print(*ans)
