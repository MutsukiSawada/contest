N = int(input())
A = [int(a) for a in input().split()]
Q = int(input())
M = [int(m) for m in input().split()]

dp = [[None] * 2000 for _ in range(N + 1)]

def solve(i, m):
    if dp[i][m] != None:
        return dp[i][m]
    if m == 0:
        dp[i][m] = True
    elif N <= i:
        dp[i][m] = False
    elif solve(i + 1, m):
        dp[i][m] = True
    elif solve(i + 1, m - A[i]):
        dp[i][m] = True
    else:
        dp[i][m] = False
    return dp[i][m]

for m in M:
    print('yes' if solve(0, m) else 'no')