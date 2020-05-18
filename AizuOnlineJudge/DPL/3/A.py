H, W = map(int, input().split())
T = [[int(t) for t in input().split()] for _ in range(H)]
A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if T[i][j] == 1:
            A[i][j] = 0
        elif i == 0 or j == 0:
            A[i][j] = 1
        else:
            A[i][j] = min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1

mx = 0
for a in A:
    mx = max(mx, max(a))

print(mx ** 2)
