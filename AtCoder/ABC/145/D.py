# D - Knight

MOD = 10 ** 9 + 7
x, y = map(int, input().split())

n, r1 = divmod(2 * y - x, 3)
m, r2 = divmod(2 * x - y, 3)

def com(n, r):
    X = Y = 1
    if r < 0 or n < r:
        return 0
    if n - r < r:
        r = n - r
    for i in range(1, r + 1):
        Y = Y * i % MOD
        X = X * (n - i + 1) % MOD
    Y = pow(Y, MOD - 2, MOD)
    return X * Y

if r1 != 0 or r2 != 0:
    print(0)
else:
    print(com(n + m, n) % MOD)
