# C - Average Length

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

D = []
for i in range(N):
    for j in range(i + 1, N):
        dist = (((P[i][0] - P[j][0]) ** 2) +
                ((P[i][1] - P[j][1]) ** 2)) ** (1 / 2)
        D.append(dist)

print(sum(D) / len(D) * (N - 1))
