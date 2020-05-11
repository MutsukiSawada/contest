# D - Teleporter

N, K = map(int, input().split())
A = [int(a) for a in input().split()]

nxt = 1
ex = 0
visited = [False] * N
repeat = []

visited[nxt - 1] = True
repeat.append(nxt)

for _ in range(N):
    nxt = A[nxt - 1]
    if visited[nxt - 1]:
        ex = repeat.index(nxt)
        repeat = repeat[ex:]
        break
    else:
        repeat.append(nxt)
        visited[nxt - 1] = True

print(repeat[(K - ex) % len(repeat)])
