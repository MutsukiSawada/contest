N = int(input())

for i in range(N):
    if i == 0:
        P = list(map(int, input().split()))
        continue
    P.append(int(input().split()[1]))

INF = 2 ** 32 - 1
dp = [[INF] * N for _ in range(N)]

for ij in range(N):
    dp[ij][ij] = 0

for l in range(1, N):
    for i in range(N):
        j = i + l
        if j >= N:
            continue
        for k in range(i, j):
            dp[i][j] = min(dp[i][k] + dp[k+1][j] + P[i] * P[j+1]*P[k+1],
                           dp[i][j])

print(dp[0][-1])
