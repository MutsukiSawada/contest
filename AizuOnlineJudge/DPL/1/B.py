N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((v, w))

C = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        item = items[i - 1]
        if item[1] <= j:
            C[i][j] = max(C[i - 1][j], C[i - 1][j - item[1]] + item[0])
        else:
            C[i][j] = C[i - 1][j]

print(C[N][W])
