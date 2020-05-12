# D - Ki

N, Q = map(int, input().split())

children = [[] for _ in range(N)]
points = [0] * N

for _ in range(N - 1):
    a, b = map(int, input().split())
    children[a - 1].append(b - 1)
    children[b - 1].append(a - 1)

for _ in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x

stack = []
stack.append(0)
visited = [False] * N
while stack:
    key = stack.pop()
    visited[key] = True
    for child in children[key]:
        if visited[child] == False:
            points[child] += points[key]
            stack.append(child)

print(*points)
