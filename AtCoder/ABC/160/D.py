# D - Line++

n, x, y = map(int, input().split())
x, y = x - 1, y - 1

cnt = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        dist = min(j - i, abs(x - i) + abs(y - j) + 1)
        cnt[dist] += 1

for i in range(1, len(cnt)):
    print(cnt[i])
