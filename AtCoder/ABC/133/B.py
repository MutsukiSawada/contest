# B - Good Distance

N, D = map(int, input().split())
X = [[int(x) for x in input().split()] for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        dist = 0
        for k in range(D):
            dist += (abs(X[i][k] - X[j][k])) ** 2
        if (dist ** (1 / 2)).is_integer():
            cnt += 1

print(cnt)
