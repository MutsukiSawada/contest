# C - Typical Stairs

MOD = (10 ** 9) + 7
N, M = map(int, input().split())
A = [False] * (N + 1)
for _ in range(M):
    A[int(input())] = True
dp = [0] * (N + 1)
dp[0] = 1
if A[1] == False:
    dp[1] = 1

for i in range(2, N + 1):
    if A[i] == True:
        dp[i] = 0
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[N])
