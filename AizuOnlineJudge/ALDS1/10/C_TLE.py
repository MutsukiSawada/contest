def lcs(X, Y):
    X = [' '] + X
    Y = [' '] + Y
    m = len(X)
    n = len(Y)
    memo = [[0] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if X[j] == Y[i]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return memo[n - 1][m - 1]

N = int(input())
for _ in range(N):
    X = [x for x in input()]
    Y = [y for y in input()]
    print(lcs(X, Y))